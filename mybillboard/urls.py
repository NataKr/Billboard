from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'board/(?P<user_name>\D+|\w+)/$', views.board, name='board'),
]

