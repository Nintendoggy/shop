from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('users/', include('ShopSystem.apps.users.urls', namespace='users')),
    path('', include('contents.urls', namespace='contents')),
    # verifications
    path('', include('verifications.urls', namespace='verifications')),
]
