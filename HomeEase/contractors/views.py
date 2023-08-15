from django.shortcuts import render, redirect
from .forms import ContractorForm

# Create your views here.

def add_contractor(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContractorForm()

    return render(request, 'add_contractor.html', {'form': form})

def success(request):
    return render(request, 'success.html')
