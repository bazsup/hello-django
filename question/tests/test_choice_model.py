from django.test import TestCase
from django.db import IntegrityError

from ..models import Choice, Question


class ChoiceModelTest(TestCase):
    def setUp(self):
        question_text = '1 + 1 = ?'
        choice_title = 'หนึ่ง'

        self.question = Question.objects.create(question=question_text)
        Choice.objects.create(question=self.question, title=choice_title)

    def test_save_data(self):
        choice = Choice.objects.last()

        self.assertEqual(choice.question.question, '1 + 1 = ?')
        self.assertEqual(choice.title, 'หนึ่ง')

    def test_unique_together_field(self):
        choice = Choice()
        choice.question = self.question
        choice.title = 'หนึ่ง'

        self.assertRaises(IntegrityError, choice.save)
