# Generated by Django 2.0.7 on 2018-08-25 19:54

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_answer_content_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]