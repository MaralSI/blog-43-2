from django.shortcuts import render, request
from django.http import HttpResponse
import random

# Create your views here.

def hello_world(request):
    return HttpResponse(f"Hello World {random.randint(0, 1000)}") # type: ignore

def main_view(request):
    return render(request,  "main.html")
