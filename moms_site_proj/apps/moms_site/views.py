from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import EmailForm

# Create your views here.
def index(request):
    form = EmailForm(request.POST)
    return render(request, 'moms_site/index.html')

# 04/02/18 - Trying to move the contact portion into the index view

def contact(request):
    messages = []
    form = EmailForm(request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        messages.append("Form is valid!")
        context = {
        'form': form
        }
        name = form.cleaned_data['name'],
        email_address = form.cleaned_data['email_address'],
        message = form.cleaned_data['message'],
        return redirect(request, 'moms_site/index.html', messages, context)
    else:
        messages.append("Form is not valid!")
        return redirect(request, 'moms_site/index.html', messages, context)


# def contact(request):
#     messages = []
#     form = EmailForm(request.POST)
#     context = {
#         'form': form
#     }
#     return redirect(request, 'moms_site/index.html', context)


