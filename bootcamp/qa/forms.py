from django import forms

from markdownx.fields import MarkdownxFormField

from bootcamp.qa.models import Question, Question2, Question3


class QuestionForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    content = MarkdownxFormField()

    class Meta:
        model = Question
        fields = ["title", "content", "tags", "status"]


class Question2Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    content = MarkdownxFormField()

    class Meta:
        model = Question2
        fields = ["title", "content", "tags", "status"]


class Question3Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    content = MarkdownxFormField()

    class Meta:
        model = Question3
        fields = ["title", "content", "tags", "status"]
