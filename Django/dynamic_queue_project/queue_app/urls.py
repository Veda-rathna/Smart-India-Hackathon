from django.urls import path
from . import views

urlpatterns = [
    path('arrive/', views.patient_arrival, name='patient_arrival'),
    path('status/', views.queue_status, name='queue_status'),
    path('queue/status/', views.queue_status, name='queue_status'),
    path('queue/clear/', views.clear_queue, name='clear_queue'),
    path('login/', views.login_view, name='login_view'),
    path('queue_status/', views.queue_status, name='queue_status'),
    path('patient_arrival/', views.patient_arrival, name='patient_arrival'),
]
