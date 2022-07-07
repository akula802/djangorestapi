from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, FailKid
from .serializers import CourseSerializer, FailKidSerializer



class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class FailKidView(viewsets.ModelViewSet):
    queryset = FailKid.objects.all()
    serializer_class = FailKidSerializer

