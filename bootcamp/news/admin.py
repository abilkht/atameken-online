from django.contrib import admin
from bootcamp.news.models import News


@admin.register(News)
class NewseAdmin(admin.ModelAdmin):
    list_display = ('content', 'content_two', 'content_three', 'content_four', 'user', 'reply')
    list_filter = ('timestamp', 'reply')
