from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
# Create your views here.

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listing.html', {'properties': properties})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')  # Change 'properties' to 'property_list'
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

