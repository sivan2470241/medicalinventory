from django.contrib import admin
from .models import Qualification,Subject,User

# Register your models here.

admin.site.register(Qualification)
admin.site.register(Subject)
admin.site.register(User)
