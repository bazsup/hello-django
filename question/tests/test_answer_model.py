from django.test import TestCase

from ..models import Answer, Choice, Question


class AnswerTest(TestCase):
    def test_save_answer(self):
        question = Question.objects.create(question='question test')
        choice = Choice.objects.create(question=question, title='choice 1')
        Answer.objects.create(question=question, selected=choice)

        answer = Answer.objects.last()

        self.assertEqual(answer.question.question, 'question test')
        self.assertEqual(answer.selected.title, 'choice 1')
