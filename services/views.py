from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, ExpertAppointment
from .forms import ExpertAppointmentForm

# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})


def book_services(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = ExpertAppointmentForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service_id = service_id 
            booking.save()

            return redirect('service_confirmation')

    else:
        form = ExpertAppointmentForm()

    return render(request, 'book_services.html', {'form': form, 'service': service})


def service_confirmation(request):
    return redirect('service_confirmation')