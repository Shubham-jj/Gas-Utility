from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceRequest
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_request_list.html'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer__user=self.request.user)

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    fields = ['request_type', 'details', 'attachment']
    template_name = 'service_request_form.html'
    success_url = reverse_lazy('service_request_list')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super().form_valid(form)

class ServiceRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRequest
    fields = ['request_type', 'details', 'attachment', 'status']
    template_name = 'service_request_form.html'
    success_url = reverse_lazy('service_request_list')

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer__user=self.request.user)

class ServiceRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRequest
    template_name = 'service_request_confirm_delete.html'
    success_url = reverse_lazy('service_request_list')

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer__user=self.request.user)