from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("hello world")


def hello(request):

    n1 = 0
    n2 = 0
    result = 0
    if request.GET:
        n1 = int(request.GET["n1"])
        n2 = int(request.GET["n2"])
        cmd = request.GET["cmd"]
        if cmd == "Add":
            result = n1 + n2
        if cmd == "Sub":
            result = n1 - n2
        if cmd == "mul":
            result = n1 * n2
        if cmd == "div":
            result = n1 / n2
        if cmd=="avg":
            result=(n1+1)/2
    return render(request, "hello.html", {"n1": n1, "n2": n2, "result": result})
