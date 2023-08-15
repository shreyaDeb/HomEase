from django.shortcuts import render
from .models import Property

# Create your views here.
def home(request):
    # Fetch featured property listings (customize the query based on your logic)
    featured_properties = Property.objects.filter(featured=True)
    return render(request, 'home.html', {'featured_properties': featured_properties})

def property_search(request):
    # Handle search bar inputs and filter properties accordingly
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    property_type = request.GET.get('property_type')

    properties = Property.objects.all()

    if location:
        properties = properties.filter(location__icontains=location)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if property_type:
        properties = properties.filter(property_type=property_type)

    return render(request, 'search_results.html', {'properties': properties})
