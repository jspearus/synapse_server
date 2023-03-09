from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('remote/', views.remote, name='remote'),
    path('room/', views.room, name='room'),
    path('term/', views.term, name='term'),
    path('red/', views.dashboard, name='dash'),
    path('hook/<str:username>/<str:msg>/<str:dest>/', views.hook, name='hook'),
]
