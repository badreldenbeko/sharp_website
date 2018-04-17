from django.core.mail import send_mail
from django.shortcuts import render, redirect

from contacts.forms import ContactForm
from services.models import Service


# Create your views here.
def home(request):
    section = 'home'
    published_services = Service.objects.all().filter(publish_on_home=True)[0:3]
    services = Service.objects.all()
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            name = contact.name
            email = contact.email
            subject = contact.subject + ' from website'
            sent_message = contact.message
            message = """
                Message from : {} \n
                Email address : {} \n
                subject : {} \n
                message : {}
            """.format(name, email, subject, sent_message)
            send_mail(subject, message, 'info@sharp4it.com', ['info@sharp4it.com'])
            contact.save()
            return redirect('/#contact')
    return render(request, 'home/home.html', {'section': section,
                                              'published_services': published_services,
                                              'services': services,
                                              'contact_form': contact_form})
