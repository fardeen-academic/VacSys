from django.contrib import admin
from .models import Member, Admin, Staff, User
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)
admin.site.register(Member)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(User)

admin.site.site_header = "VacSys Admin Portal"
admin.site.site_title = "VacSys Admin Portal"
admin.site.index_title = "Welcome to VacSys Admin Portal"

