import re
from tkinter import Variable
from django.shortcuts import render
from django.http import HttpResponse

from home.models import SigUpMembers

# Create your views here.

def sigUpMembers : _QureySet[Any, Dic[str,Any]]
 sigUpMembers = SignUpMembers.objects.all().values()
return HttpResponse(sigUpMembers)

def index(request):

    return HttpResponse("Hello Moheed!")

#def index1(request):
 #   return HttpResponse("Hello Moheed Aziz!")