from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def resume(request):
    return render(request, 'main/resume.html')

def about(request):
    return render(request, 'main/about.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def skills(request):
    return render(request, 'main/skills.html')

def diplomas(request):
    return render(request, 'main/diplomas.html')

def contacts(request):
    return render(request, 'main/contacts.html')