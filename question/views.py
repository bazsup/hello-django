from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answer, Choice
from .forms import QuizForm
import json
from django.views import View

class QuestionView(View):
    def post(self, request):
        # print('length', request.POST)
        length = request.POST.get('question_length')
        # for x in list(request.POST):
            # print(x)
        # print('length', length)
        # print('array', length.split(','))
        # result = ''
        for question_pk in length.split(','):
            selected_choices = request.POST.getlist('question_id_' + question_pk)
            question = Question.objects.get(pk=question_pk)
            # print('question', question)
            for selected_choice_pk in selected_choices:
                choice = Choice.objects.get(pk=selected_choice_pk)
                # print(question_pk, ': ', selected_choice_pk)
                Answer.objects.create(question=question, selected=choice)
            result += 'question' + question_pk + ': ' + str(request.POST.getlist('question_id_' + question_pk)) + '<br />'
        result += '<a href="/answer">ไปดูเฉลยหน่อยซิ กดเบา ๆ นะ</a>'
        return HttpResponse('Thanks <br/>' + result)


def question(request):
    form = QuizForm()
    questions = Question.objects.all()
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
    return render(request, 'question.html', { 'question_list': question_list, 'form': form, 'question_keys': keys })

def answer(request):
    answers = list(Answer.objects.all())
    return render(request, 'answer.html', { 'answers': answers })

def reset_answer(request):
    Answer.objects.all().delete()
    return redirect('/answer')