from django.contrib import admin
from .models import User, UserProfile, Gender

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
