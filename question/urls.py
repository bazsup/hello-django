from django.urls import path

from . import views
from question import views as questionView
from question.views import QuestionView

urlpatterns = [
    path('question/', QuestionView.as_view()),
    path('answer/', questionView.answer),
    path('answer/reset/', questionView.reset_answer),
]