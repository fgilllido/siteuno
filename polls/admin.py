from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#admin.site.register(Question)
#admin.site.register(Choice)

#class ChoiceInLine(admin.StackedInline):
 
class ChoiceInLine(admin.TabularInline):   
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub', 'question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date','es_reciente')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
