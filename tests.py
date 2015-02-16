# -*- coding: utf8 -*-

from coverage import coverage
from os.path import abspath
from os.path import dirname
from library.models import Question, Answer, User

cov = coverage(branch=True, omit=['venv/*', 'tests.py'])
cov.start()

import os
import unittest
from datetime import datetime


from library import app, db


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(dirname(abspath(__file__)), 'test.sqlite')
        db.create_all()
        self.auth = {"username": "test", "password": "123"}
        self.user = User(login='user',
                         password='111')
        self.q = Question(title='hi',
                          text=u'How are you?',
                          timestamp=datetime.utcnow(),
                          user_id=1)
        self.answer = Answer(text='Good', user_id=1, q_id=1, timestamp=datetime.utcnow())
        db.session.add(self.user)
        db.session.add(self.q)
        db.session.add(self.answer)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_models(self):
        self.assertEqual(self.user.login, 'user')
        self.assertEqual(self.user.password, '111')
        self.assertEqual(self.q.title, 'hi')
        self.assertEqual(self.q.text, u'How are you?')
        self.assertEqual(self.q.user_id, 1)
        self.assertEqual(self.answer.text, 'Good')
        self.assertEqual(self.answer.user_id, 1)
        self.assertEqual(self.answer.q_id, 1)

    def test_user(self):
        # create a user
        u = User(login='john', password='111')
        db.session.add(u)
        db.session.commit()
        assert u.is_authenticated() is True
        assert u.is_active() is True
        assert u.is_anonymous() is False
        assert u.id == int(u.get_id())

    def test_question(self):
        # create a question
        u = Question(title='I want to know', text='something about a Sun', timestamp=datetime.utcnow())
        db.session.add(u)
        db.session.commit()
        assert u.title == 'I want to know'
        assert u.text == 'something about a Sun'
        assert u.id == int(u.get_id())

    def test_answer(self):
        # create an answer
        u = Answer(text='john know about everything', timestamp=datetime.utcnow(), q_id=1)
        db.session.add(u)
        db.session.commit()
        assert u.text == 'john know about everything'
        assert u.vote is 0
        assert u.id == int(u.get_id())


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print "\n\nCoverage Report:\n"
    cov.report()
    print "\nHTML version: " + os.path.join(dirname(abspath(__file__)), "tmp/coverage/index.html")
    cov.html_report(directory='tmp/coverage')
    cov.erase()