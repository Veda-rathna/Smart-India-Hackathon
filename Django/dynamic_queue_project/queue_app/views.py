from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Patient, Queue
from .forms import PatientForm
from django.contrib import messages
from queue_app.models import Queue
from django.contrib.auth.views import LoginView
from .models import PatientQueue

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Default credentials for demonstration purposes
        if role == 'user' and username == 'user' and password == 'user':
            return redirect('queue_status')
        elif role == 'admin' and username == 'admin' and password == 'admin':
            return redirect('patient_arrival')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_view')

    return render(request, 'login.html')

def queue_status(request):
    queue = PatientQueue.objects.order_by('-priority')
    return render(request, 'queue_status.html', {'queue': queue})

def patient_arrival(request):
    return render(request, 'patient_arrival.html')

def patient_arrival(request):
    if request.method == 'POST':
        # Assuming you have a form to capture the patient's name, condition severity, and expected service time
        name = request.POST.get('name')
        condition_severity = int(request.POST.get('condition_severity'))
        expected_service_time = int(request.POST.get('expected_service_time'))

        # Create new patient and add to queue
        patient = Patient.objects.create(name=name, condition_severity=condition_severity, expected_service_time=expected_service_time)
        queue = Queue.objects.create(patient=patient)

        return redirect('queue_status')
    
    return render(request, 'queue_app/patient_arrival.html')

def queue_status(request):
    # Fetch all patients in the queue
    queue = Queue.objects.all()

    # Update priority for each patient based on their condition and waiting time
    for item in queue:
        item.update_priority()

    # Sort by priority (lower number = higher priority)
    sorted_queue = sorted(queue, key=lambda x: x.priority)

    context = {
        'queue': sorted_queue
    }
    
    return render(request, 'queue_app/queue_status.html', context)

def home_view(request):
    return render(request, 'home.html') 

def clear_queue(request):
    if request.method == 'POST':
        Queue.objects.all().delete()
        messages.success(request, 'Queue has been cleared successfully.')
    return redirect('queue_status')

def nearby_hospitals(request):
    return render(request, 'queue_app/nearby_hospitals.html')