from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    email = EmailMessage('title', 'body', to=[email])
    email.send()
    return render(request, 'smtp/index.html')