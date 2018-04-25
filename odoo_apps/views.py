from django.shortcuts import render, redirect
from .models import OdooApps
from .forms import AppsForm


# Create your views here.
def app_list(request):
    apps = OdooApps.objects.all()
    app_form = AppsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if app_form.is_valid():
            app_form.save()
            return redirect('odoo-apps:list')
    return render(request, 'apps/list.html', {'apps': apps, 'app_form': app_form})
