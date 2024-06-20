from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

"""
Assumption: The web application is intended for the use of the students in a specific university. Therefore, the `Username` shall be their respectively assigned Student/Faculty Numbers
"""


class UserManager(BaseUserManager):
    def create_user(
        self, username, email_address, role, password=None, *args, **kwargs
    ):
        """
        Create, save, and return a new User.
        """
        if not username:
            raise ValueError("The `username` field must be set.")
        if not email_address:
            raise ValueError("The `email_address` field must be set.")

        # Normalize the given email_address (turns the domain part of the email to lowercase, e.g. `example@GMAIL.com` to `example@gmail.com`)
        email_address = self.normalize_email(email_address)
        user = self.model(
            username=username, email_address=email_address, role=role, *args, **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, role, password=None, **extra_fields):
        """
        Create, save, and return a new User that is Superuser.
        """

        extra_fields.setDefault("is_staff", True)
        extra_fields.setDefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have `is_staff` = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have `is_superuser` = True.")

        return self.create_user(username, email, role, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for User. Contains the essential credentials for authorization and authentication.
    """

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "FACULTY", "Faculty"

    # Fields
    username = models.CharField(
        verbose_name="Username",
        max_length=50,
        unique=True,
        help_text="Student or Faculty ID Number",
    )
    email_address = models.EmailField(
        verbose_name="Email Address", max_length=100, unique=True
    )
    role = models.CharField(verbose_name="Role", max_length=50, choices=Role.choices)
    is_active = models.BooleanField(verbose_name="Active", default=True)
    is_staff = models.BooleanField(verbose_name="Staff Status", default=False)
    date_joined = models.DateField(verbose_name="Date Joined", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Updated At", auto_now=True, blank=False
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email_address", "role"]

    objects = UserManager()

    def is_admin(self):
        return self.role == "ADMIN"

    def is_faculty(self):
        return self.role == "FACULTY"

    def is_student(self):
        return self.role == "STUDENT"

    def __str__(self):
        return self.username


class Gender(models.Model):
    """
    A model for assigning Gender to user instances.
    """

    gender_name = models.CharField(verbose_name="Gender", max_length=20)


class UserProfile(models.Model):
    """
    A model intended for storing the personal details of a user instance. This includes their name, address, etc.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(verbose_name="First Name", max_length=50, blank=False)
    middle_name = models.CharField(
        verbose_name="Middle Name", max_length=50, blank=False
    )
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=False)
    suffix = models.CharField(
        verbose_name="Suffix",
        max_length=10,
        null=True,
        help_text="Name suffix e.g. I, II, III. Leave blank if none.",
    )
    date_of_birth = models.DateField(verbose_name="Birthdate")
    contact_number = models.CharField(
        verbose_name="Contact Number", max_length=16, help_text="+63-xxx-xxxx-xxx"
    )
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)
    permanent_address = models.TextField(
        verbose_name="Permanent Address",
        max_length=255,
        help_text="No. | Street | Barangay | City/Town | Zip Code",
    )

    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.middle_name} {self.last_name}"
