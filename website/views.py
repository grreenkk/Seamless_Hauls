from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})
# Create your views here.

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        message = "Name: " + message_name \
                  + " Email: " + message_email \
                  +  " Message " + message


        send_mail(
            'Service Request', # subject
            message, # message
            message_email, # from email
            ['seamlesshauls@gmail.com'], # To Email
            )

        return render(request, 'contact_us2.html', {'message_name': message_name})
    else:
        return render(request, 'contact_us2.html', {})


def about(request):
    return render(request, 'about_us.html', {})
