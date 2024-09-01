from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)  # Higher value means higher priority

    def __str__(self):
        return self.name

class Queue(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service_time = models.DateTimeField()  # Time when the patient is expected to be served

    def __str__(self):
        return f"{self.patient.name} at {self.service_time}"
