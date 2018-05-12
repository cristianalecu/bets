from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restuser import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.RestUserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.RestUserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)