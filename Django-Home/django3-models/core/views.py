from django.shortcuts import render
from core.models import Students

# Create your views here.
# QuerySets contains all the objects inside a model.
# all() --> returns  a copy of querySet
def home(req):
    stu_rec = Students.objects.all()
    std_rgd = Students.objects.filter(city = 'rgdd').first() # get() --> particular value
    
    std = {
        "rec":stu_rec,
        "rgd":std_rgd
    }

    return render(req, "core/base.html", std)