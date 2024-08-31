from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'beds', views.BedViewSet)
router.register(r'wards', views.WardViewSet)
router.register(r'medicines', views.MedicineViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'admissions', views.AdmissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
