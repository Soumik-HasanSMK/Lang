from django.shortcuts import render

def func(request):
    return render(request, 'home.html')