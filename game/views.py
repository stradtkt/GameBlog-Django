from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'game/index.html', context)
