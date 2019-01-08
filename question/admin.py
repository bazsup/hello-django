from django.contrib import admin

from .models import Question, Choice, Answer

admin.site.register(Question)

admin.site.register(Choice)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created',
        'modified',
    ]

    def title(self, object):
        return object.question.question + ' (' + object.selected.title + ') '
