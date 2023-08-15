from django import forms
from .models import Contractor

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'services', 'contact_email', 'phone_country_code', 'phone_number']
