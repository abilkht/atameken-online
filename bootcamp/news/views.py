from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DeleteView
from django.shortcuts import render
import django_tables2 as tables
from django_tables2 import RequestConfig

from bootcamp.helpers import ajax_required, AuthorRequiredMixin
from bootcamp.news.models import News


class NewsTable(tables.Table):
    class Meta:
        model = News
        fields = ('content', 'content_two', 'content_three', 'content_four')
        attrs = {'class': 'table table-hover'}
        template_name = 'django_tables2/semantic.html'


def tablify(request):
    table = NewsTable(News.objects.all())
    # table = NewsTable(News.objects.values_list('content', 'content_two', 'content_three', 'content_four', named=True))
    RequestConfig(request).configure(table)
    return render(request, 'news/news_table.html', {'table': table})


class NewsListView(LoginRequiredMixin, ListView):
    """A really simple ListView, with some JS magic on the UI."""
    model = News
    paginate_by = 15

    def get_queryset(self, **kwargs):
        return News.objects.filter(reply=False)


class NewsDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    """Implementation of the DeleteView overriding the delete method to
    allow a no-redirect response to use with AJAX call."""
    model = News
    success_url = reverse_lazy("news:list")


@login_required
@ajax_required
def post_news(request):
    """A function view to implement the post functionality with AJAX allowing
    to create News instances as parent ones."""
    if request.method == 'POST':
        user = request.user
        post = request.POST['post']
        post2 = request.POST['post2']
        post3 = request.POST['post3']
        post4 = request.POST['post4']

        post = post.strip()
        post2 = post2.strip()
        post3 = post3.strip()
        post4 = post4.strip()

        if 0 < len(post) and len(post2) and (len(post3) and len(post4)) <= 1000:
            posted = News.objects.create(
                user=user,
                content=post,
                content_two=post2,
                content_three=post3,
                content_four=post4,
            )
            html = render_to_string(
                'news/news_single.html',
                {
                    'news': posted,
                    'request': request,
                })
            return HttpResponse(html)

        else:
            length = len(post) - 1000
            return HttpResponseBadRequest(
                content=_(f'Текст {length} слишком большой или пустой.'))

    else:
        return HttpResponseBadRequest(content=_('Wrong request type.'))


@login_required
@ajax_required
def like(request):
    """Function view to receive AJAX, returns the count of likes a given news
    has received."""
    if request.method == 'POST':
        news_id = request.POST['news']
        news = News.objects.get(pk=news_id)
        user = request.user
        news.switch_like(user)
        return JsonResponse({"likes": news.count_likers()})

    else:
        return HttpResponseBadRequest(content=_('Wrong request type.'))


@login_required
@ajax_required
def get_thread(request):
    """Returns a list of news with the given news as parent."""
    news_id = request.GET['news']
    news = News.objects.get(pk=news_id)
    news_html = render_to_string("news/news_single.html", {"news": news})
    thread_html = render_to_string(
        "news/news_thread.html", {"thread": news.get_thread()})
    return JsonResponse({
        "uuid": news_id,
        "news": news_html,
        "thread": thread_html,
    })


@login_required
@ajax_required
def post_comment(request):
    """A function view to implement the post functionality with AJAX, creating
    News instances who happens to be the children and commenters of the root
    post."""
    if request.method == 'POST':
        user = request.user
        post = request.POST['reply']
        par = request.POST['parent']
        parent = News.objects.get(pk=par)
        post = post.strip()
        if post:
            parent.reply_this(user, post)
            return JsonResponse({'comments': parent.count_thread()})

        else:
            return HttpResponseBadRequest()

    else:
        return HttpResponseBadRequest(content=_('Wrong request type.'))


@login_required
@ajax_required
def update_interactions(request):
    data_point = request.POST['id_value']
    news = News.objects.get(pk=data_point)
    data = {'likes': news.count_likers(), 'comments': news.count_thread()}
    return JsonResponse(data)
