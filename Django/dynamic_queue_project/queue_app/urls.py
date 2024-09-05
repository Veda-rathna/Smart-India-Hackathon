from django.urls import path
from . import views

urlpatterns = [
    path('arrive/', views.patient_arrival, name='patient_arrival'),
    path('status/', views.queue_status, name='queue_status'),
    path('queue/status/', views.queue_status, name='queue_status'),
    path('queue/clear/', views.clear_queue, name='clear_queue'),
]
