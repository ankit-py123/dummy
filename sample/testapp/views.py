from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request):
    return HttpResponse("<h1>Hello Python...</h1>")

def raks(request):
    return HttpResponse("<h1>राकेश चे भांडे. </h2>")
