# Generated by Django 2.0.7 on 2018-09-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0017_auto_20180901_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer2',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer3',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer4',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer5',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer6',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer7',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AddField(
            model_name='answer8',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question2',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question3',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question4',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question5',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question6',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
        migrations.AlterField(
            model_name='question7',
            name='file',
            field=models.FileField(blank=True, upload_to='forum_files/%Y/%m/%d/', verbose_name='Загрузить файл'),
        ),
    ]