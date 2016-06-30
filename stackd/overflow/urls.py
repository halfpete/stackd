from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/', views.post, name='post'),
    url(r'login/', views.user_login, name='user_login'),
    url(r'register/', views.register, name='register'),
    url(r'logout/', views.user_logout, name='user_logout'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<comment_id>[0-9]+)/tu$', views.thumbup_comment, name='tuc'),
    url(r'^(?P<comment_id>[0-9]+)/td$', views.thumbdown_comment, name='tdc'),
    url(r'^(?P<question_id>[0-9]+)/q/tu$', views.thumbup_question, name='tuq'),
    url(r'^(?P<question_id>[0-9]+)/q/td$', views.thumbdown_question, name='tdq'),
    url(r'^(?P<answer_id>[0-9]+)/a/tu$', views.thumbup_answer, name='tua'),
    url(r'^(?P<answer_id>[0-9]+)/a/td$', views.thumbdown_answer, name='tda'),
]
