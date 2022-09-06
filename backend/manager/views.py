from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def say_hello(request):
    return HTTPResponse('Hello World')