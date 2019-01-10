from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('question', 'title'))


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected = models.ForeignKey(Choice, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question.question + ' (' + self.selected.title + ') '
