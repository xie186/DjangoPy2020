from django.shortcuts import render
from django.http import HttpResponse

# MVT: model view template (Django)
# MVC: model view controller
# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at the polll index")

