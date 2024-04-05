from django.shortcuts import render, redirect
from .models import ExpertAppointment
from .forms import ExpertAppointmentForm

# Create your views here.

def expertise(request):
    if request.method == 'POST':
        form = ExpertAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_expert')

    else:
        form = ExpertAppointmentForm()
        return render(request, 'expertise.html', {'form': form})