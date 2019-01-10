from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .models import Question, Answer, Choice
from .forms import QuestionForm, QuestionFormset


class QuestionView(View):
    def post(self, request):
        question_pks = request.POST.get('question_pks')
        html = ''
        for question_pk in question_pks.split(','):
            selected_choices = request.POST.getlist(
                'question_id_' + question_pk
            )
            question = Question.objects.get(pk=question_pk)
            for selected_choice_pk in selected_choices:
                choice = Choice.objects.get(pk=selected_choice_pk)
                Answer.objects.create(question=question, selected=choice)
            html += 'question %s: %s<br />' % (question_pk, str(request.POST.getlist('question_id_'+question_pk)))
        html += '<a href="/answer">ไปดูเฉลยหน่อยซิ กดเบา ๆ นะ</a>'
        return HttpResponse('Thanks <br/>' + html)

    def get(self, request):
        questions = Question.objects.all()
        form = QuestionFormset()
        # form = QuestionForm(questions=questions)
        question_list = []
        question_keys = []
        for question in questions:
            choices_per_question = list(Choice.objects.filter(question=question))
            prepare_data = {
                'question_pk': question.pk,
                'question': question.question,
                'choices': choices_per_question
            }
            question_list.append(prepare_data)
            question_keys.append(str(question.pk))
        keys = ','.join(question_keys)
        return render(request, 'question.html', {'question_list': question_list, 'form': form, 'question_keys': keys})


def answer(request):
    answers = list(Answer.objects.all())
    return render(request, 'answer.html', {'answers': answers})


def reset_answer(request):
    if request.method == 'POST':
        Answer.objects.all().delete()
    return redirect('/answer')
