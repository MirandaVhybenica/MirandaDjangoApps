from django.urls import path
from . import views

urlpatterns = [
    
    path('portfolio/',views.portfolio, name="portfolio"),
    
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]