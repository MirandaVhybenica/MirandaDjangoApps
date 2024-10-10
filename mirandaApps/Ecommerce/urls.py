from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('index/',views.index, name="index"),
    
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contacts/', views.contacts, name='contacts'),
]

