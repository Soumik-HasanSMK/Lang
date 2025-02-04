from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of ProjactName.</h1>")

def navbar(request):
    return render(request,"index.html")

def about(request):
    d={"name": "spam", "age":11, "arr":[1,2,3,4,5,6,7,8,9]}
    return render(request,"index.html",d)