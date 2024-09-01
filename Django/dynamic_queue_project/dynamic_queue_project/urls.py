# dynamic_queue_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs
from queue_app import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('queue/', include('queue_app.urls')),  # Include app's URLs from queue_app/urls.py
    path('', views.home_view, name='home_view'),  # Root URL pattern
]
