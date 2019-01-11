from django.test import TestCase
from django.urls import reverse

from ..models import Choice, Question


class QuestionGetViewTests(TestCase):
    def test_question_response_return_correctly(self):
        question = Question.objects.create(question='1 + 1 = ?')
        choice = Choice.objects.create(question=question, title='หนึ่ง')

        last_question = Question.objects.last()
        last_choice = Choice.objects.last()
        expected = [
            {
                'question_pk': last_question.pk,
                'question': last_question.question,
                'choices': [last_choice]
            }
        ]

        response = self.client.get(reverse('question'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1 + 1 = ?")

        question_context = response.context['question_list']
        self.assertEqual(question_context, expected)
