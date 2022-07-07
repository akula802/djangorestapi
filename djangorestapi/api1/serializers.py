from rest_framework import serializers
from .models import Course, FailKid


# Serializer for the Course class
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')



# Serializer for the FailKid class
class FailKidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FailKid
        fields = ('id', 'url', 'fk_name', 'fk_grade')
