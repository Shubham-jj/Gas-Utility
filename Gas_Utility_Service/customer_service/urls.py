from django.urls import path
from .views import ServiceRequestListView, ServiceRequestCreateView

urlpatterns = [
    path('requests/', ServiceRequestListView.as_view(), name='service_request_list'),
    path('requests/new/', ServiceRequestCreateView.as_view(), name='service_request_create'),
]