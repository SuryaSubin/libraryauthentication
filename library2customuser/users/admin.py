from django.contrib import admin
from users.models import CustomUser,Users
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Users)