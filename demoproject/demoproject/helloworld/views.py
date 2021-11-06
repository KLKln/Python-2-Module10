from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!, from Kelly Klein on 10/30/2021')

# Create your views here.
