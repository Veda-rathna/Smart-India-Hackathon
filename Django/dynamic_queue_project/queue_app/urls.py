from django.urls import path
from . import views

urlpatterns = [
    path('queue/status/', views.queue_status, name='queue_status'),
    path('queue/clear/', views.clear_queue, name='clear_queue'),
    path('queue_status/', views.queue_status, name='queue_status'),
    path('patient_arrival/', views.patient_arrival, name='patient_arrival'),
]
