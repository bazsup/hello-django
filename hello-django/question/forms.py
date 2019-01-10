from django import forms
from django.forms import formset_factory

from .models import Answer, Choice, Question


class QuestionForm(forms.ModelForm):
    # answers = forms.BooleanField()
    # choices = forms.BooleanField()
    

    class Meta:
        model = Answer
        fields = '__all__'


QuestionFormset = formset_factory(QuestionForm, extra=1)
