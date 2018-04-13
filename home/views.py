from django.shortcuts import render

from services.models import Service


# Create your views here.
def home(request):
    section = 'home'
    published_services = Service.objects.all().filter(publish_on_home=True)[0:3]
    services = Service.objects.all()
    return render(request, 'home/home.html', {'section': section,
                                              'published_services': published_services,
                                              'services': services})
