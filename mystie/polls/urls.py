from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       #polls
    url(r'^$', views.IndexView.as_view(), name='index'),
                       #polls/number
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       #polls/number/resuts
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name="results"),
                       #polls/number/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
