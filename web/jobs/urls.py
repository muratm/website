from django.conf.urls import patterns, url

from jobs.views import JobsView, CreateJobView, JobDetailView


urlpatterns = patterns(
    '',
    url(r'^$', JobsView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)', JobDetailView.as_view(), name='detail'),
    url(r'^new$', CreateJobView.as_view(), name='new'),
)
