from distutils.command.clean import clean
from django.shortcuts import render
from .forms import Denote_information_Form, send_message_Form
# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        form=send_message_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'sform': send_message_Form})
        else :
            form=send_message_Form()
    return render(request, 'contact.html', {'sform': send_message_Form})


def home_page(request):
    return render(request, 'home.html')


def donores_page(request):
    return render(request, 'donors.html')


def Registration_page(request):

    if request.method == 'POST':
        form = Denote_information_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'Registration.html', {'rform': Denote_information_Form, 'ok': True})
        else:
            print(form.errors.as_data())
            form = Denote_information_Form()

    return render(request, 'Registration.html', {'rform': Denote_information_Form, 'ok': False})



