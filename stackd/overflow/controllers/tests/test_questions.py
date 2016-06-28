from django.test import TestCase
from overflow.models import Question
from overflow.controllers.questions import upvote_question, downvote_question

class DummyTest(TestCase):
    def test_dummy(self):
        self.assertEquals(1, 1)


class QuestionTestCase(TestCase):
    def test_adding_question(self):
        question = Question()
        question.author = 'hh'
        self.assertEqual(question.author, 'hh')

    def test_upvote_question(self):
        question = Question()
        upvote_question(question)
        self.assertEqual(question.upvotes, 1)

    def test_downvote_question(self):
        question = Question()
        downvote_question(question)
        self.assertEqual(question.downvotes, 1)

    def test_netvotes_question(self):
        question = Question()
        downvote_question(question)
        downvote_question(question)
        downvote_question(question)
        self.assertEqual(question.netvotes(), -3)
        upvote_question(question)
        upvote_question(question)
        upvote_question(question)
        upvote_question(question)
        self.assertEqual(question.netvotes(), 1)



