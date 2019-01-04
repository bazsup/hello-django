from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer, Choice
from .forms import QuizForm
import json
from django.views import View

class QuestionView(View):
    def post(self, request):
        print('************************')
        # question_length = eval(request.POST.question_length)

        print('length', request.POST)
        length = request.POST.get('question_length')
        for x in list(request.POST):
            print(x)
        print('length', length)
        print('array', length.split(','))
        result = ''
        for key in length.split(','):
            print('question', key, ': ', str(request.POST.getlist('question_id_' + key)))
            result += 'question' + key + ': ' + str(request.POST.getlist('question_id_' + key)) + '<br />'
        print('************************')
        return HttpResponse('Thanks <br/>' + result)


def question(request):
    if request.method == "POST":
        
        form = QuizForm(request.POST)
        print('***** valid form ********')
        print(form)
        # print(form.cleaned_data)
        print('*************')

        if form.is_valid():
            print('isValid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponse('thanks !' if form.is_valid() else 'Invalid form')
    else:
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
        print(keys)
        return render(request, 'question.html', { 'question_list': question_list, 'form': form, 'question_keys': keys })

def answer(request):
    return render(request, 'answer.html')