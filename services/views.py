from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, BookService
from .forms import BookServiceForm

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


def book_service(request, service_id): 
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = BookServiceForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service
            booking.save()

            return redirect('service_confirmation', booking_id=booking.id)

    else:
        form = BookServiceForm()

    return render(request, 'book_services.html', {'form': form, 'service': service})


def service_confirmation(request, booking_id):
    booking = get_object_or_404(BookService, id=booking_id)
    messages.success(request, f'Your booking of {booking.service.name} was made successfully! \
        Your booking ID is {booking_id}.')

    template = 'service_confirmation.html'
    context = {'booking': booking}
    return render(request, template, context)