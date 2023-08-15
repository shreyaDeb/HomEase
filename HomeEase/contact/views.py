from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactMessage

# Create your views here.

def contact(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('You got a mail!', message, '', ['shreya.deb.1602@gmail.com']) # TODO: enter your email address
        
    return render(request, 'contact.html', {})