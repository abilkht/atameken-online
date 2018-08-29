from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseBadRequest, JsonResponse
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from bootcamp.helpers import ajax_required
from bootcamp.qa.models import Question, Answer, Question2, Answer2, Question3, Answer3, Question4, Answer4, Question5, Answer5, Question6, Answer6, Question7, Answer7, Question8, Answer8
from bootcamp.qa.forms import QuestionForm, Question2Form, Question3Form, Question4Form, Question5Form, Question6Form, Question7Form, Question8Form


class FakeIndexView(TemplateView):
    """View to render the fake index page."""
    template_name = "qa/question_fake_main.html"


class IndexView(TemplateView):
    """View to render the index page."""
    template_name = "qa/question_main.html"


class QuestionsIndexListView(LoginRequiredMixin, ListView):
    """CBV to render a list view with all the registered questions."""
    model = Question
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question.objects.get_counted_tags()
        context["active"] = "all"
        return context


class QuestionAnsListView(QuestionsIndexListView):
    """CBV to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class QuestionListView(QuestionsIndexListView):
    """CBV to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class QuestionDetailView(LoginRequiredMixin, DetailView):
    """View to call a given Question object and to render all the details about
    that Question."""
    model = Question
    context_object_name = "question"
    template_name = "qa/question_detail.html"


class CreateQuestionView(LoginRequiredMixin, CreateView):
    """
    View to handle the creation of a new question
    """
    form_class = QuestionForm
    template_name = "qa/question_form.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans")


class CreateAnswerView(LoginRequiredMixin, CreateView):
    """
    View to create new answers for a given question
    """
    model = Answer
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail", kwargs={"pk": self.kwargs["question_id"]})


class Questions2IndexListView(LoginRequiredMixin, ListView):
    """CBV [2] to render a list with all the registered questions."""
    model = Question2
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_2.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question2.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question2AnsListView(Questions2IndexListView):
    """CBV [2] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question2.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question2ListView(Questions2IndexListView):
    """CBV [2] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question2.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question2DetailView(LoginRequiredMixin, DetailView):
    """View [2] to call a given Question object and to render all the details about
    that Question."""
    model = Question2
    context_object_name = "question"
    template_name = "qa/question_detail_2.html"


class CreateQuestion2View(LoginRequiredMixin, CreateView):
    """
    View [2] to handle the creation of a new question
    """
    form_class = Question2Form
    template_name = "qa/question_form_2.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans2")


class CreateAnswer2View(LoginRequiredMixin, CreateView):
    """
    View [2] to create new answers for a given question
    """
    model = Answer2
    fields = ["content", ]
    template_name = "qa/answer_form_2.html"

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail2", kwargs={"pk": self.kwargs["question_id"]})


class Questions3IndexListView(LoginRequiredMixin, ListView):
    """CBV [3] to render a list with all the registered questions."""
    model = Question3
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_3.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question3.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question3AnsListView(Questions3IndexListView):
    """CBV [3] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question3.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question3ListView(Questions3IndexListView):
    """CBV [3] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question3.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question3DetailView(LoginRequiredMixin, DetailView):
    """View [3] to call a given Question object and to render all the details about
    that Question."""
    model = Question3
    context_object_name = "question"
    template_name = "qa/question_detail_3.html"


class CreateQuestion3View(LoginRequiredMixin, CreateView):
    """
    View [3] to handle the creation of a new question
    """
    form_class = Question3Form
    template_name = "qa/question_form_3.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans3")


class CreateAnswer3View(LoginRequiredMixin, CreateView):
    """
    View [3] to create new answers for a given question
    """
    model = Answer3
    template_name = "qa/answer_form_3.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail3", kwargs={"pk": self.kwargs["question_id"]})


class Questions4IndexListView(LoginRequiredMixin, ListView):
    """CBV [4] to render a list with all the registered questions."""
    model = Question4
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_4.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question4.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question4AnsListView(Questions4IndexListView):
    """CBV [4] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question4.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question4ListView(Questions4IndexListView):
    """CBV [4] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question4.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question4DetailView(LoginRequiredMixin, DetailView):
    """View [4] to call a given Question object and to render all the details about
    that Question."""
    model = Question4
    context_object_name = "question"
    template_name = "qa/question_detail_4.html"


class CreateQuestion4View(LoginRequiredMixin, CreateView):
    """
    View [4] to handle the creation of a new question
    """
    form_class = Question4Form
    template_name = "qa/question_form_4.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans4")


class CreateAnswer4View(LoginRequiredMixin, CreateView):
    """
    View [4] to create new answers for a given question
    """
    model = Answer4
    template_name = "qa/answer_form_4.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail4", kwargs={"pk": self.kwargs["question_id"]})


class Questions5IndexListView(LoginRequiredMixin, ListView):
    """CBV [5] to render a list with all the registered questions."""
    model = Question5
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_5.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question5.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question5AnsListView(Questions5IndexListView):
    """CBV [5] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question5.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question5ListView(Questions5IndexListView):
    """CBV [5] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question5.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question5DetailView(LoginRequiredMixin, DetailView):
    """View [5] to call a given Question object and to render all the details about
    that Question."""
    model = Question5
    context_object_name = "question"
    template_name = "qa/question_detail_5.html"


class CreateQuestion5View(LoginRequiredMixin, CreateView):
    """
    View [5] to handle the creation of a new question
    """
    form_class = Question5Form
    template_name = "qa/question_form_5.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans5")


class CreateAnswer5View(LoginRequiredMixin, CreateView):
    """
    View [5] to create new answers for a given question
    """
    model = Answer5
    template_name = "qa/answer_form_5.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail5", kwargs={"pk": self.kwargs["question_id"]})


class Questions6IndexListView(LoginRequiredMixin, ListView):
    """CBV [6] to render a list with all the registered questions."""
    model = Question6
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_6.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question6.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question6AnsListView(Questions6IndexListView):
    """CBV [6] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question6.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question6ListView(Questions6IndexListView):
    """CBV [6] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question6.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question6DetailView(LoginRequiredMixin, DetailView):
    """View [6] to call a given Question object and to render all the details about
    that Question."""
    model = Question6
    context_object_name = "question"
    template_name = "qa/question_detail_6.html"


class CreateQuestion6View(LoginRequiredMixin, CreateView):
    """
    View [6] to handle the creation of a new question
    """
    form_class = Question6Form
    template_name = "qa/question_form_6.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans6")


class CreateAnswer6View(LoginRequiredMixin, CreateView):
    """
    View [6] to create new answers for a given question
    """
    model = Answer6
    template_name = "qa/answer_form_6.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail6", kwargs={"pk": self.kwargs["question_id"]})


class Questions7IndexListView(LoginRequiredMixin, ListView):
    """CBV [7] to render a list with all the registered questions."""
    model = Question7
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_7.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question7.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question7AnsListView(Questions7IndexListView):
    """CBV [7] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question7.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question7ListView(Questions7IndexListView):
    """CBV [7] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question7.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question7DetailView(LoginRequiredMixin, DetailView):
    """View [7] to call a given Question object and to render all the details about
    that Question."""
    model = Question7
    context_object_name = "question"
    template_name = "qa/question_detail_7.html"


class CreateQuestion7View(LoginRequiredMixin, CreateView):
    """
    View [7] to handle the creation of a new question
    """
    form_class = Question7Form
    template_name = "qa/question_form_7.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans7")


class CreateAnswer7View(LoginRequiredMixin, CreateView):
    """
    View [7] to create new answers for a given question
    """
    model = Answer7
    template_name = "qa/answer_form_7.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail7", kwargs={"pk": self.kwargs["question_id"]})


class Questions8IndexListView(LoginRequiredMixin, ListView):
    """CBV [8] to render a list with all the registered questions."""
    model = Question8
    paginate_by = 20
    context_object_name = "questions"
    template_name = "qa/question_list_8.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["popular_tags"] = Question8.objects.get_counted_tags()
        context["active"] = "all"
        return context


class Question8AnsListView(Questions8IndexListView):
    """CBV [8] to render a list view with all question which have been already
    marked as answered."""

    def get_queryset(self, **kwargs):
        return Question8.objects.get_answered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "answered"
        return context


class Question8ListView(Questions8IndexListView):
    """CBV [8] to render a list view with all question which haven't been marked
    as answered."""

    def get_queryset(self, **kwargs):
        return Question8.objects.get_unanswered()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["active"] = "unanswered"
        return context


class Question8DetailView(LoginRequiredMixin, DetailView):
    """View [8] to call a given Question object and to render all the details about
    that Question."""
    model = Question8
    context_object_name = "question"
    template_name = "qa/question_detail_8.html"


class CreateQuestion8View(LoginRequiredMixin, CreateView):
    """
    View [8] to handle the creation of a new question
    """
    form_class = Question8Form
    template_name = "qa/question_form_8.html"
    message = _("Ваш вопрос создан.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse("qa:index_noans8")


class CreateAnswer8View(LoginRequiredMixin, CreateView):
    """
    View [8] to create new answers for a given question
    """
    model = Answer8
    template_name = "qa/answer_form_8.html"
    fields = ["content", ]

    # message = _("Спасибо! Ваш ответ опубликован.")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs["question_id"]
        return super().form_valid(form)

    def get_success_url(self):
        # messages.success(self.request, self.message)
        return reverse(
            "qa:question_detail8", kwargs={"pk": self.kwargs["question_id"]})


@login_required
@ajax_required
def question_vote(request):
    """Function view to receive AJAX call, returns the count of votes a given
    question has recieved."""
    if request.method == "POST":
        question_id = request.POST["question"]
        value = None
        if request.POST["value"] == "U":
            value = True

        else:
            value = False

        question = Question.objects.get(pk=question_id)
        try:
            question.votes.update_or_create(
                user=request.user, defaults={"value": value}, )
            question.count_votes()
            return JsonResponse({"votes": question.total_votes})

        except IntegrityError:
            return JsonResponse({'status': 'false',
                                 'message': _("Database integrity error.")},
                                status=500)

    else:
        return HttpResponseBadRequest(content=_("Wrong request type."))


@login_required
@ajax_required
def answer_vote(request):
    """Function view to receive AJAX call, returns the count of votes a given
    answer has recieved."""
    if request.method == "POST":
        answer_id = request.POST["answer"]
        value = None
        if request.POST["value"] == "U":
            value = True

        else:
            value = False

        answer = Answer.objects.get(uuid_id=answer_id)
        try:
            answer.votes.update_or_create(
                user=request.user, defaults={"value": value}, )
            answer.count_votes()
            return JsonResponse({"votes": answer.total_votes})

        except IntegrityError:
            return JsonResponse({'status': 'false',
                                 'message': _("Database integrity error.")},
                                status=500)

    else:
        return HttpResponseBadRequest(content=_("Wrong request type."))


@login_required
@ajax_required
def accept_answer(request):
    """Function view to receive AJAX call, marks as accepted a given answer for
    an also provided question."""
    if request.method == "POST":
        answer_id = request.POST["answer"]
        answer = Answer.objects.get(uuid_id=answer_id)
        answer.accept_answer()
        return JsonResponse({'status': 'true'}, status=200)

    else:
        return HttpResponseBadRequest(content=_("Wrong request type."))
