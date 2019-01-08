from django.test import TestCase

from ..admin import AnswerAdmin


class AnswerAdminTest(TestCase):
    def test_model_should_have_list_display(self):
        expected = ['title', 'created', 'modified']

        self.assertEqual(AnswerAdmin.list_display, expected)