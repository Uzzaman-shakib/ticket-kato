from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='theater-home'),
    path('nowshowing/', views.nowshowing, name='theater-nowshowing'),
    path('ticketprice/', views.ticketprice, name='theater-ticketprice'),
    path('about/', views.about, name='theater-about'),
    path('aynabji/', views.aynabaji, name='aynabaji'),
    path('contact/', views.contact, name='contact'),
]