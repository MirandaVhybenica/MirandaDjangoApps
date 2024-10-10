from django.shortcuts import render

def portfolio(request):
    context={}
    return render(request, "Portfolio/portfolio.html", context)

def about(request):
    return render(request, 'Portfolio/about.html')

def projects(request):
    return render(request, 'Portfolio/projects.html')

def contact(request):
    return render(request, 'Portfolio/contact.html')
