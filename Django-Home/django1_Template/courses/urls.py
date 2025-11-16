from django.urls import path
from courses.views import home, profile

urlpatterns = [
    path('', home),
    path ('profile/', profile)

]