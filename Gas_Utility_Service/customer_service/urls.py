from django.urls import path
from .views import ServiceRequestListView, ServiceRequestCreateView
from .views import ServiceRequestUpdateView, ServiceRequestDeleteView

urlpatterns = [
    path('requests/', ServiceRequestListView.as_view(), name='service_request_list'),
    path('requests/new/', ServiceRequestCreateView.as_view(), name='service_request_create'),
    path('requests/<int:pk>/edit/', ServiceRequestUpdateView.as_view(), name='service_request_update'),
    path('requests/<int:pk>/delete/', ServiceRequestDeleteView.as_view(), name='service_request_delete'),
]