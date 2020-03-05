from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateTimeField('date of birth')
    sex = models.CharField(max_length=200)   

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Doctor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    date_hire = models.DateTimeField('date hired')
    
    def how_long_employed(self):
        return timezone.now() - self.date_hire

    def __str__(self):
        return self.title + " " + self.first_name

class Record(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.PROTECT,
                               help_text="The patient associated with this record")

    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,
                               help_text="The doctor that entered this record.")

    visit_date = models.DateTimeField(help_text='date of visit.')
    
    description = models.CharField(max_length=500, default=None,
        help_text="Describe reason for patient visit.")
    
    prescription = models.CharField(max_length=500, default=None,
        help_text="Input any medication prescribed to patient by doctor.")

    follow_up_care = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")

    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return str(self.patient) + ' experiencing ' + self.description