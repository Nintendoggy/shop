from django.urls import path, include, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    re_path('usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/', views.UsernameCountView.as_view()),
    re_path('mobiles/(?P<mobile>1[3-9]\d{9})/count/', views.MobileCountView.as_view()),
]