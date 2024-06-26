# Generated by Django 5.0.6 on 2024-06-20 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gender_name", models.CharField(max_length=20, verbose_name="Gender")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="Student or Faculty ID Number",
                        max_length=50,
                        unique=True,
                        verbose_name="Username",
                    ),
                ),
                (
                    "email_address",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Email Address"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("STUDENT", "Student"),
                            ("FACULTY", "Faculty"),
                        ],
                        max_length=50,
                        verbose_name="Role",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Staff Status"),
                ),
                (
                    "date_joined",
                    models.DateField(auto_now_add=True, verbose_name="Date Joined"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "middle_name",
                    models.CharField(max_length=50, verbose_name="Middle Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "suffix",
                    models.CharField(
                        help_text="Name suffix e.g. I, II, III. Leave blank if none.",
                        max_length=10,
                        null=True,
                        verbose_name="Suffix",
                    ),
                ),
                ("date_of_birth", models.DateField(verbose_name="Birthdate")),
                (
                    "contact_number",
                    models.CharField(
                        help_text="+63-xxx-xxxx-xxx",
                        max_length=16,
                        verbose_name="Contact Number",
                    ),
                ),
                (
                    "permanent_address",
                    models.TextField(
                        help_text="No. | Street | Barangay | City/Town | Zip Code",
                        max_length=255,
                        verbose_name="Permanent Address",
                    ),
                ),
                (
                    "gender_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.gender"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
