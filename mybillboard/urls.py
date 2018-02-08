from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'board/$', views.board, name='board'),
    url(r'board/post/$', views.add_post, name='add_post'),
    url(r'board/messages/(?P<user>\D+|\w+|\W+)/$', views.user_view, name='user_view'),
    url(r'board/get_comments/$', views.get_comments, name='get_comments'),
    url(r'board/delete/$', views.remove_message, name='remove_message'),
    url(r'^$', views.index, name='index'),
]
