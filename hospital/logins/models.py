from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('General Physician', 'General Physician'),
        ('Pediatrician', 'Pediatrician'),
    ]
    name = models.CharField(max_length=100, null=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" if self.user else "Guest Patient"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    patient_email = models.EmailField(null=True, blank=True)
    patient_phone = models.CharField(max_length=15, null=True, blank=True)
    appointment_date = models.CharField(max_length=15)
    appointment_time = models.CharField(max_length=15)
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} on {self.appointment_date} at {self.appointment_time}"

    class Meta:
        unique_together = ['doctor', 'appointment_date', 'appointment_time']


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    feedback = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback from {self.name or self.user.username if self.user else 'Anonymous'} on {self.created_at.strftime('%Y-%m-%d')}"


