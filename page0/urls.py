from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('score', views.score, name='Score Page'),
    path('play', views.play, name='Game Page'),
    path('submit', views.receive, name='Submit'),
    path('create', views.create, name='Create Ques'),
    path('list', views.upload_all_ques, name='List Question')
]