from django.test import TestCase
from overflow.models import Question, Comment
from overflow.controllers.comments import upvote_question, downvote_question


class QuestionTestCase(TestCase):
    def test_adding_comment(self):
        comment = Comment()
        comment.author = 'hh'
        self.assertEqual(comment.author, 'hh')