from django.shortcuts import render

# Create your views here.
def django(req):
    return render(req, "course/django.html")

def python(req):
    return render(req, "course/python.html")

def web(req):
    return render(req, "course/web.html")
