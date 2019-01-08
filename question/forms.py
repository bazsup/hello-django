import json

from django import forms

from .models import Question, Choice, Answer

class QuizForm(forms.ModelForm):

    # def __init__(self):
    answers = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, label=u"Please select a answer:")

    class Meta:
        model = Answer
        fields = ()