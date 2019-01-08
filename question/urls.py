from django.urls import path

from question import views as questionView
from question.views import QuestionView

urlpatterns = [
    path('question/', QuestionView.as_view(), name="question"),
    path('answer/', questionView.answer),
    path('answer/reset/', questionView.reset_answer),
]
