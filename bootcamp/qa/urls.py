from django.conf.urls import url

from bootcamp.qa import views

app_name = 'qa'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='question_main'),
    url(r'^question-list/$', views.QuestionListView.as_view(), name='index_noans'),
    url(r'^question-list-2/$', views.Question2ListView.as_view(), name='index_noans2'),
    url(r'^question-list-3/$', views.Question3ListView.as_view(), name='index_noans3'),
    url(r'^answered/$', views.QuestionAnsListView.as_view(), name='index_ans'),
    url(r'^answered-2/$', views.Question2AnsListView.as_view(), name='index_ans2'),
    url(r'^answered-3/$', views.Question3AnsListView.as_view(), name='index_ans3'),
    url(r'^indexed/$', views.QuestionsIndexListView.as_view(), name='index_all'),
    url(r'^indexed-2/$', views.Questions2IndexListView.as_view(), name='index_all2'),
    url(r'^indexed-3/$', views.Questions3IndexListView.as_view(), name='index_all3'),
    url(r'^question-detail/(?P<pk>\d+)/$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question-detail-2/(?P<pk>\d+)/$', views.Question2DetailView.as_view(), name='question_detail2'),
    url(r'^question-detail-3/(?P<pk>\d+)/$', views.Question3DetailView.as_view(), name='question_detail3'),
    url(r'^ask-question/$', views.CreateQuestionView.as_view(), name='ask_question'),
    url(r'^ask-question-2/$', views.CreateQuestion2View.as_view(), name='ask_question2'),
    url(r'^ask-question-3/$', views.CreateQuestion3View.as_view(), name='ask_question3'),
    url(r'^propose-answer/(?P<question_id>\d+)/$', views.CreateAnswerView.as_view(), name='propose_answer'),
    url(r'^propose-answer-2/(?P<question_id>\d+)/$', views.CreateAnswer2View.as_view(), name='propose_answer2'),
    url(r'^propose-answer-3/(?P<question_id>\d+)/$', views.CreateAnswer3View.as_view(), name='propose_answer3'),
    url(r'^question/vote/$', views.question_vote, name='question_vote'),
    url(r'^answer/vote/$', views.answer_vote, name='answer_vote'),
    url(r'^accept-answer/$', views.accept_answer, name='accept_answer'),
]
