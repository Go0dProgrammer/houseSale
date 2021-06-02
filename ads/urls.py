from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('<str:slug>', views.AdDetail.as_view(), name='ad_detail'),
]