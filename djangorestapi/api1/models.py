from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    # Just so the admin section doesn't just show (Course Obect 1, etc)
    def __str__(self):
        return self.name



class FailKid(models.Model):
    fk_name = models.CharField(max_length=200)
    fk_grade = models.CharField(max_length=4)

    def __str__(self):
        return self.fk_name
