from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'pages/home.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)