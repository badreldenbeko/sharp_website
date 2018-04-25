from django.shortcuts import render, redirect, get_object_or_404
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


def app_delete(request, slug):
    app = get_object_or_404(OdooApps, slug=slug)
    if request.method == 'POST':
        app.delete()
        return redirect('odoo-apps:list')
    return render(request, 'apps/delete.html', {'app': app})
