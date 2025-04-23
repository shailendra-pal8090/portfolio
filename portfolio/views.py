from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')
def skills(request):
    return render(request, 'skills.html')