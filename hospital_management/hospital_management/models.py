from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    available_beds = models.IntegerField()

    def __str__(self):
        return self.name

class Bed(models.Model):
    ward = models.ForeignKey(Ward, related_name='beds', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('occupied', 'Occupied')])
    patient = models.OneToOneField('Patient', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ward.name} - Bed {self.id}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Appointment {self.id} with {self.doctor.name}"

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    bed = models.OneToOneField(Bed, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Admission {self.id} of {self.patient.name}"
