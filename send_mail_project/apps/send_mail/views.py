from django.shortcuts import render, redirect
from send_mail.forms import ContactForm

# Create your views here.
def index(request):
    form_class = ContactForm
    context = {
        'form_class': form,
    }
    return render(request, 'send_mail/index.html')