from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactCreateForm
from .models import Contact
from services.models import Service


# Create your views here.
@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get('query')
    services = Service.objects.all()
    replayed = request.GET.get('replayed')
    contact_form = ContactCreateForm(request.POST or None, request.FILES or None)
    if query:
        contacts = contacts.filter(Q(name__icontains=query) | Q(email__contains=query))
        if replayed == '1':
            contacts = contacts.filter(Q(replayed=True))
        if replayed == '0':
            contacts = contacts.filter(Q(replayed=False))
    if replayed == '1':
        contacts = contacts.filter(Q(replayed=True))
        if query:
            contacts = contacts.filter(Q(name__icontains=query) | Q(email__contains=query))
    if replayed == '0':
        contacts = contacts.filter(Q(replayed=False))
        if query:
            contacts = contacts.filter(Q(name__icontains=query) | Q(email__contains=query))
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact:list')
    return render(request, 'contacts/list.html',
                  {'contacts': contacts, 'services': services, 'contact_form': contact_form})


@login_required
def contact_delete(request, slug):
    contact = get_object_or_404(Contact, slug=slug)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:list')
    return render(request, 'contacts/delete.html', {'contact': contact})


@login_required
def contact_edit(request, slug=None):
    if slug:
        contact = get_object_or_404(Contact, slug=slug)
        contact_form = ContactCreateForm(request.POST or None, request.FILES or None, instance=contact)
        services = Service.objects.all()
        if request.method == 'POST':
            if contact_form.is_valid():
                contact_form.save()
            return redirect('contact:list')
        return render(request, 'contacts/edit.html',
                      {'contact': contact, 'contact_form': contact_form, 'services': services})
