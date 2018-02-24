from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'', views.home, name='home'),
    url(r'play', views.play, name='play'),
    url(r'leaderboard/', views.leaderboard, name='leaderboard'),
    url(r'submission-result/<int:attempted_question_pk>/', views.submission_result, name='submission_result'),
]
