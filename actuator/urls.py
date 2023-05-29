from django.urls import path, include
from actuator import views

urlpatterns = [
    # actuator/
    path('healthcheck/', views.healthcheck),
    path('healthcheck/<status>/', views.healthcheck),
]
