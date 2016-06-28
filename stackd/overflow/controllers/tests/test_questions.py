from django.test import TestCase
from stackd.overflow.models import Question


class DummyTest(TestCase):
    def test_dummy(self):
        self.assertEquals(1, 1)

# class QuestionTestCase(TestCase):
    # def test_adding_question(self):
    #     question = Question()
    #     question.author = 'hh'
    #     self.assertEqual(question.author, 'hh')
