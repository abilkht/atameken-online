from django import forms

from markdownx.fields import MarkdownxFormField

from bootcamp.qa.models import Question, Question2, Question3, Question4, Question5, Question6, Question7, Question8


class QuestionForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField(verbose_name='Контент')

    class Meta:
        model = Question
        fields = ["title", "content", "tags", "status", "file"]


class Question2Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question2
        fields = ["title", "content", "tags", "status", "file"]


class Question3Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question3
        fields = ["title", "content", "tags", "status", "file"]


class Question4Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question4
        fields = ["title", "content", "tags", "status", "file"]


class Question5Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question5
        fields = ["title", "content", "tags", "status", "file"]


class Question6Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question6
        fields = ["title", "content", "tags", "status", "file"]


class Question7Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question7
        fields = ["title", "content", "tags", "status", "file"]


class Question8Form(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    # content = MarkdownxFormField()

    class Meta:
        model = Question8
        fields = ["title", "content", "tags", "status", "file"]
