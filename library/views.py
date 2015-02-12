# -*- coding: utf-8 -*-
import datetime
from flask.ext.babel import gettext
from flask.ext.login import login_required, logout_user, login_user, current_user
from library import app, db, lm
from flask import render_template, flash, g, url_for, redirect, request, abort
from library.forms import QuestionForm, LoginForm, RegistrationForm, AnswerForm
from .models import Question, User, Answer

POSTS_PER_PAGE = 5
OFFSET = 15


@lm.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:page>', methods=['GET', 'POST'])
def home(page=1):
    form = QuestionForm()
    if form.validate_on_submit():
        q = Question(title=form.title.data,
                     text=form.text.data,
                     timestamp=datetime.datetime.utcnow(),
                     user_id=g.user.get_id()
                     )
        try:
            db.session.add(q)
            db.session.commit()
            flash(gettext('You are posted the question!'), category='success')
        except Exception as e:
            db.session.rollback()
            flash(e, category='error')
        return redirect(url_for('home'))
    questions = Question.query.order_by(Question.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template('start.html', questions=questions, form=form, page=page)


@app.route('/question/<int:id>', methods=('GET', 'POST'))
def view(id, page=1):
    q = Question.query.get(id)
    if q is None:
        flash('Question not found.', category='error')
        return redirect(url_for('home'))
    answers = Answer.query.filter_by(q_id=id).order_by(Answer.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(text=form.text.data, q_id=q.id,
                        timestamp=datetime.datetime.utcnow(),
                        user_id=g.user.get_id())
        try:
            db.session.add(answer)
            db.session.commit()
            flash(gettext('You are posted the answer!'), category='success')
        except Exception as e:
            db.session.rollback()
            flash(e, category='error')
        return redirect(url_for('view', id=id))
    return render_template('question.html', question=q, form=form, answers=answers, page=page)


@app.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    link = '<p>Already have an account? <a href="' + url_for('login') + '">Click here to log in.</a></p>'
    if form.validate_on_submit():
        user = User(form.login.data, unicode(form.password.data))
        form.populate_obj(user)
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Congratulation! You are registered successfully.', category='success')
        except Exception as e:
            db.session.rollback()
            flash(e, category='error')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, link=link)


@app.route("/login", methods=('GET', 'POST'))
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    link = '<p>Don\'t have an account? <a href="' + url_for('register') + '">Click here to register.</a></p>'
    if form.validate_on_submit():
        user = form.get_user()
        login_user(user)
        flash("Logged in successfully.", category='success')
    if current_user.is_authenticated():
        return redirect(url_for('home'))
    return render_template("login.html", form=form, link=link)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/answers', methods=['GET', 'POST'])
@app.route('/answers/<int:page>', methods=['GET', 'POST'])
def answers(page=1):
    answers = Answer.query.order_by(Answer.timestamp.desc()).paginate(page, POSTS_PER_PAGE, OFFSET)
    return render_template('answers.html', answers=answers, page=page)


@app.route('/voting', methods=['GET', 'POST'])
@login_required
def voting():
    id = request.args.get('id', None)
    q_id = request.args.get('q_id', None)
    if not id or not q_id:
        abort(404)
    answer = Answer.query.get_or_404(int(id))
    try:
        answer.upvote()
        db.session.add(answer)
        db.session.commit()
        flash('You are voted successfully. Thank you.', category='success')
    except Exception as e:
        db.session.rollback()
        flash(e, category='error')
    return redirect(url_for('view', id=q_id))