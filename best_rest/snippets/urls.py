from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)