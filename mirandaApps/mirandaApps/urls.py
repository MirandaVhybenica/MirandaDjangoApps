
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ecommerce.urls')),
    path('', include('Portfolio.urls')),
    path('', include('Shop.urls')),
    
]
