from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3/0
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
