from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  myText = "Welcome to Hill Bakes"
  return HttpResponse(myText)