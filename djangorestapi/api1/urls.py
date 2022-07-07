# api1 urls.py

from django.urls import path, include
from . import views
from rest_framework import routers


# Create the routers, these allow GET and POST requests
router = routers.DefaultRouter()
router.register('courses', views.CourseView)


# The string in the 'register' defines the URL at which this API can be accessed
router2 = routers.DefaultRouter()
router.register('failkids', views.FailKidView)



# Ok the URLs go here
urlpatterns = [
    path('', include(router.urls)),
]
