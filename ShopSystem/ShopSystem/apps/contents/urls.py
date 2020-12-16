# 子路由配置
from django.urls import path

from ShopSystem.apps.contents import views

app_name = 'contents'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
