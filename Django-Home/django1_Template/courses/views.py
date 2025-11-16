from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def profile(request):
    dict = {"name" : "pranav kumar",
            "age" : 22, 
            "gender" : "male",
            "qualification" : "Master of Computer Application", 
            "hobbies" : "Photography, Adventure, learn new things",
            "language" : ["C", "java", "python", "PHP", "Html", "Css", "Javascript", "Sql"]
            }
    return render(request, "courses/profile.html", dict)

# Create your views here.

