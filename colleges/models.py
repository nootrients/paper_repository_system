from django.db import models


# Create your models here.
class RegionalGroup(models.Model):
    name = models.CharField(verbose_name="Region Name", max_length=50)

    def __str__(self):
        return self.name


class UniversityBranch(models.Model):
    name = models.CharField(verbose_name="University Branch", max_length=50)
    regional_group = models.ForeignKey(
        RegionalGroup,
        verbose_name="Regional Group",
        on_delete=models.CASCADE,
        related_name="branches",
    )

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name="Department Name", max_length=50)

    def __str__(self):
        return self.name


class BranchDepartment(models.Model):
    branch = models.ForeignKey(
        UniversityBranch, on_delete=models.CASCADE, related_name="branch_departments"
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="branch_departments"
    )
    email_address = models.EmailField(verbose_name="Email Address", max_length=50)
    contact_number = models.CharField(verbose_name="Contact Number", max_length=20)

    def __str__(self):
        return f"{self.branch.name} - {self.department.name}"


class Course(models.Model):
    title = models.CharField(verbose_name="Course", max_length=200)
    branch_department = models.ForeignKey(
        UniversityBranch, on_delete=models.CASCADE, related_name="courses"
    )

    def __str__(self):
        return self.course_name
