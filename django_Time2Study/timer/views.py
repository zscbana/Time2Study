from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def timer(request):
    return render(request, "timer/timer.html", {'title': 'StudySession'})

def status(request):
    return render(request, 'timer/status.html', {'title': 'profile'})