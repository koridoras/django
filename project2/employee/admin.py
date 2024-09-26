from django.contrib import admin
from .models import Department, Employee, Status

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Status)