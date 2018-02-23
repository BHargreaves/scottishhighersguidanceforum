from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This will be the home page")

def subjectIndex(request):
    return HttpResponse("This will be the subject index page")

