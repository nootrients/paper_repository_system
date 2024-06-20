from django.db import models


# Create your models here.
class RegionalGroup(models.Model):
    region_name = models.CharField(verbose_name="Region Name", max_length=50)

    def __str__(self):
        return self.region_name


class UniversityBranch(models.Model):
    branch_name = models.CharField(verbose_name="University Branch", max_length=50)
    regional_group = models.ForeignKey(
        RegionalGroup, verbose_name="Regional Group", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.branch_name


class Course(models.Model):
    course_name = models.CharField(verbose_name="Course", max_length=200)
    branches = models.ManyToManyField(UniversityBranch, related_name="courses")

    def __str__(self):
        return self.course_name
