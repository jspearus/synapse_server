from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('red/', views.redthumb, name='red'),
    path('remote/', views.remote, name='remote'),
    path('room/', views.room, name='room'),
    path('<str:room_name>/', views.term, name='terminal'),
    path('hook/<str:username>/<str:msg>/<str:dest>/', views.hook, name='hook'),
]
