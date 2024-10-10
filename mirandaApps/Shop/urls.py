from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration, name="registration"),
    
    path('login/', views.login, name='login'),
    path('lpage/', views.lpage, name='lpage'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),
    path('edit/', views.edit, name='edit'),
]
