from django.core.mail import send_mail
from django.shortcuts import render, redirect

from contacts.forms import ContactForm
from contacts.models import Contact
from services.models import Service, ServiceClient


# Create your views here.
def home(request):
    section = 'home'
    published_services = Service.objects.all().filter(publish_on_home=True)[0:3]
    services = Service.objects.all()
    contact_form = ContactForm()
    clients = ServiceClient.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            name = cd['en_contact_name']
            email = cd['email']
            subject = cd['subject'] + ' from website'
            sent_message = cd['message']
            message = """
                Message from : {} \n
                Email address : {} \n
                subject : {} \n
                message : {}
            """.format(name, email, subject, sent_message)
            send_mail(subject, message, 'info@sharp4it.com', ['info@sharp4it.com'])
            contact = Contact.objects.filter(email=email)
            if not contact:
                Contact.objects.create(en_contact_name=name, email=email, subject=subject, message='message')
                return redirect('/#contact')
            else:
                contact.subject = subject
                contact.message = message
                contact.save()
                return redirect('/#contact')
    return render(request, 'home/home.html', {'section': section,
                                              'published_services': published_services,
                                              'services': services,
                                              'contact_form': contact_form,
                                              'clients': clients})
