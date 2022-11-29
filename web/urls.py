from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('remote/', views.remote, name='remote'),
    path('<str:room_name>/', views.term, name='terminal'),
    path('hook/<str:username>/<str:msg>/<str:dest>/', views.hook, name='hook'),
]
