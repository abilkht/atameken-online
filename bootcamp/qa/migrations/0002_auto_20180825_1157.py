# Generated by Django 2.0.7 on 2018-08-25 11:57

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content_two',
            field=markdownx.models.MarkdownxField(default='null'),
        ),
        migrations.AddField(
            model_name='question',
            name='title_two',
            field=models.CharField(default='asd', max_length=200),
        ),
    ]