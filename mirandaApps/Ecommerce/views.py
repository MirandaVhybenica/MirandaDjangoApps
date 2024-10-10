from django.shortcuts import render

def index(request):
    context={}
    return render(request, "Ecommerce/index.html", context)

def home(request):
    return render(request, 'Ecommerce/home.html')

def shop(request):
    return render(request, 'Ecommerce/shop.html')

def aboutus(request):
    return render(request, 'Ecommerce/aboutus.html')

def contacts(request):
    return render(request, 'Ecommerce/contacts.html')
