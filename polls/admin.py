from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#admin.site.register(Question)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub', 'question_text']

admin.site.register(Question, QuestionAdmin)
