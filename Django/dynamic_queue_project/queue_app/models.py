from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Patient(models.Model):
    name = models.CharField(max_length=100)
    condition_severity = models.IntegerField()  # Higher severity = Higher priority
    arrival_time = models.DateTimeField(auto_now_add=True)
    expected_service_time = models.IntegerField()  # in minutes
    priority = models.IntegerField(default=0)  # Priority field (higher value = higher priority)

    def update_priority(self):
        # Ensure arrival_time is timezone-aware
        if timezone.is_naive(self.arrival_time):
            arrival_time = timezone.make_aware(self.arrival_time)
        else:
            arrival_time = self.arrival_time

        # Get the current timezone-aware time
        current_time = timezone.now()

        # Calculate the time waited
        time_waited = current_time - arrival_time
        wait_time_in_minutes = time_waited.total_seconds() / 60

        # Update priority based on severity and wait time
        self.priority = self.condition_severity * wait_time_in_minutes
        self.save()
        
    def calculate_actual_service_time(self):
        # Adjust logic to calculate the actual service time based on severity
        severity_factor = 1 if self.condition_severity > 5 else 2
        return self.expected_service_time / severity_factor

    def assign_priority(self):
        # Example: priority is calculated based on severity and how long the patient has been waiting
        wait_time_minutes = (timezone.now() - self.arrival_time).total_seconds() / 60
        self.priority = self.condition_severity + int(wait_time_minutes // 10)  # Add 1 point of priority for every 10 minutes of waiting
        self.save()

    def __str__(self):
        return self.name


class Queue(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)
    arrival_time = models.DateTimeField(default=timezone.now)

    def update_priority(self):
        # Ensure arrival_time is timezone-aware
        if timezone.is_naive(self.arrival_time):
            arrival_time = timezone.make_aware(self.arrival_time)
        else:
            arrival_time = self.arrival_time

        # Get the current timezone-aware time
        current_time = timezone.now()

        # Calculate the wait time
        time_waited = current_time - arrival_time

        # Convert to minutes
        wait_time_in_minutes = time_waited.total_seconds() / 60

        # Access condition_severity through the related patient
        patient_severity = self.patient.condition_severity

        # Calculate priority based on condition_severity and wait time
        self.priority = patient_severity * wait_time_in_minutes
        self.save()


    def __str__(self):
        return f"{self.patient.name} (Priority: {self.priority})"
