from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:company>/', views.client, name='client'),
]