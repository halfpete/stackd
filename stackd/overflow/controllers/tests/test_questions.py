from django.test import TestCase
from overflow.models import Question
from overflow.controllers.questions import upvote, downvote


class QuestionTestCase(TestCase):
    def test_adding_question(self):
        question = Question()
        question.author = 'hh'
        self.assertEqual(question.author, 'hh')

    def test_upvote_question(self):
        question = Question()
        upvote(question)
        self.assertEqual(question.upvotes, 1)

    def test_downvote_question(self):
        question = Question()
        downvote(question)
        self.assertEqual(question.downvotes, 1)

    def test_netvotes_question(self):
        question = Question()
        downvote(question)
        downvote(question)
        downvote(question)
        self.assertEqual(question.netvotes(), -3)
        upvote(question)
        upvote(question)
        upvote(question)
        upvote(question)
        self.assertEqual(question.netvotes(), 1)



