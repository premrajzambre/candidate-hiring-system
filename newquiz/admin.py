#page admin de dJango http://localhost:8000/admin

from django.contrib import admin
from newquiz.models import Option, Question

class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)
