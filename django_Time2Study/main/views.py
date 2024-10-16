from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})

def roadmap(request):
    return render(request, 'main/roadmap.html', {'title': 'Roadmap'})

def study(request):
    return render(request, 'main/study.html', {'title': 'StudyTime'})