from django.contrib import admin
from bootcamp.qa.models import Question, Answer, Question2, Answer2, Question3, Answer3, Question4, Answer4, Question5, Answer5, Question6, Answer6, Question7, Answer7, Question8, Answer8


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question2)
class Question2Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question3)
class Question3Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question4)
class Question4Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question5)
class Question5Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question6)
class Question6Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question7)
class Question7Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
    list_filter = ('user', 'has_answer')


@admin.register(Question8)
class Question8Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'slug', 'status', 'content', 'has_answer', 'total_votes', 'file')
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


@admin.register(Answer4)
class Answer4Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer5)
class Answer5Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer6)
class Answer6Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer7)
class Answer7Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')


@admin.register(Answer8)
class Answer8Admin(admin.ModelAdmin):
    list_display = ('question', 'user', 'content', 'uuid_id', 'is_answer')
    list_filter = ('user', 'is_answer')