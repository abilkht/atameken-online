from django.contrib import admin
from bootcamp.qa.models import Question, Answer, Question2, Answer2, Question3, Answer3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes')
    list_filter = ('user', 'has_answer')


@admin.register(Question2)
class Question2Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes')
    list_filter = ('user', 'has_answer')


@admin.register(Question3)
class Question3Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes')
    list_filter = ('user', 'has_answer')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer2)
class Answer2Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer3)
class Answer3Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')