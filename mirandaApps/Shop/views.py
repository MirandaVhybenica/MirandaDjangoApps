from django.shortcuts import render

def registration(request):
    context={}
    return render(request, "Shop/registration.html", context)

def login(request):
    return render(request, 'Shop/login.html')

def lpage(request):
    return render(request, 'Shop/lpage.html')

def profile(request):
    return render(request, 'Shop/profile.html')

def history(request):
    return render(request, 'Shop/history.html')

def edit(request):
    return render(request, 'Shop/edit.html')