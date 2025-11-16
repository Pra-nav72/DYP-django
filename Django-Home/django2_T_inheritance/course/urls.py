from django.urls import path
from course.views import django, python, web

urlpatterns = [
    path('dj/', django, name='dj'),
    path('py/', python, name='py'),
    path('web/', web, name='web')
]
