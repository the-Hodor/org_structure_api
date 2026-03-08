from django.contrib import admin

from django.contrib import admin
from .models import Organization, Department, Employee

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Employee)
