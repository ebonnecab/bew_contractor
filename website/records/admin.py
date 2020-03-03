from django.contrib import admin
from .models import Record, Patient, Doctor

# Register your models here.
admin.site.register(Record)
admin.site.register(Patient)
admin.site.register(Doctor)