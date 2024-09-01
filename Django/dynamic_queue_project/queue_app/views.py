from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Patient, Queue
from .forms import PatientForm

def patient_arrival(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            # Define the service time dynamically, e.g., based on queue length or priority
            service_time = timezone.now() + timezone.timedelta(minutes=10)
            Queue.objects.create(patient=patient, service_time=service_time)
            return redirect('queue_status')
    else:
        form = PatientForm()
    return render(request, 'queue_app/patient_arrival.html', {'form': form})

def queue_status(request):
    queue = Queue.objects.order_by('service_time')
    return render(request, 'queue_app/queue_status.html', {'queue': queue})

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html') 
