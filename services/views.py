from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, BookService
from .forms import BookServiceForm, ServiceForm
from products.forms import ProductForm


# Create your views here.
def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


@login_required
def add_service(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service = service_form.save()
            messages.success(request, 'Successfully added service!')
            return redirect('services')
        else:
            messages.error(request, 'Failed to add service,'
                                    'please ensure the form is valid.')
    else:
        service_form = ServiceForm()
    product_form = ProductForm()
    return render(request, 'add_product.html', {'service_form': service_form, 'product_form': product_form})


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

    return render(request,
                  'book_services.html', {'form': form, 'service': service})


def service_confirmation(request, booking_id):
    booking = get_object_or_404(BookService, id=booking_id)
    messages.success(request,
                     f'Your booking of {booking.service.name} '
                     f'was made successfully!Your booking ID is {booking_id}.')
    template = 'service_confirmation.html'
    context = {'booking': booking}
    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('services'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to update service. '
                           'Please ensure that the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('services'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Successfully deleted service!')
    return redirect(reverse('services'))
