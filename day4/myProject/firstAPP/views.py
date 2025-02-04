from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    lst=[1,2,3,4,5,6,7,8,9,10]
    d={"lst":lst, "str1":"kjasdhkajdk", "str2":"AKJSFKJWFKLJFF", "str3":"ipsum dolor sit amet, pharetra felis neque eu lectus."}

    #two types of returns
    return render(request, 'app.html',d)
    # return render(request, 'app.html', {"lst":lst, "str1":"kjasdhkajdk", "str2":"AKJSFKJWFKLJFF", "str3":"ipsum dolor sit amet, pharetra felis neque eu lectus."})


def test2(request):
    a=10+20
    # return HttpResponse("This is test2")
    return HttpResponse(a)
    # return HttpResponse("<p>this is in p tags</p>")