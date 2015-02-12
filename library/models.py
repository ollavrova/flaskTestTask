# -*- coding: utf-8 -*-
from flask.ext.login import UserMixin
from library import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def check_password(self, passw):
        return self.password == passw

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return '<User %r>' % (self.login)


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    text = db.Column(db.Text(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)

    def get_id(self):
        return self.id

    @property
    def get_user(self):
        return User.query.get(int(self.user_id))

    @property
    def get_answers_count(self):
        return Answer.query.filter(Answer.q_id == self.id).count()

    def __unicode__(self):
        return '<Question %d>' % self.id


class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    q_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    timestamp = db.Column(db.DateTime)
    vote = db.Column(db.Integer, default=0)

    def upvote(self):
        self.vote = self.vote + 1
        return self.vote

    def get_id(self):
        return self.id

    @property
    def get_user(self):
        return User.query.get(int(self.user_id))

    def __unicode__(self):
        return '<Answer %d>' % self.id
