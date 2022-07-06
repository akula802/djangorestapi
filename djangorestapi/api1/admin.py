from django.contrib import admin
from .models import Course
from .models import FailKid #A test model and class I added for understanding


admin.site.register(Course)
admin.site.register(FailKid)