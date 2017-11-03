from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, template_name="views/index.html")

def Funkcja():
    for x in range(0, 10):
        print(x)

def Funkcja1(request):
   text = "<h1>welcome to my app number %s!</h1>"
   return HttpResponse(text)


def Funkcja2(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)




