from django.db import models


# Create your models here.
class UniversityBranch(models.Model):
    branch_name = models.CharField(verbose_name="University Branch", max_length=50)

    def __str__(self):
        return self.branch_name


class Course(models.Model):
    course_name = models.CharField(verbose_name="Course", max_length=200)
    branches = models.ManyToManyField(UniversityBranch, related_name="courses")

    def __str__(self):
        return self.course_name
