# polls/admin.py
from django.contrib import admin
from .models import Question, Choice
from .models import Question, Choice, Comment

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)