from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactReplayForm
from .models import Contact


def replayed(contacts, replayed=None):
    if replayed:
        contacts.filter(Q(replayed=True))
    else:
        contacts.filter(Q(replayed=False))
    return contacts


# Create your views here.
@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get('query')
    replayed = request.GET.get('replayed')
    if query:
        contacts = contacts.filter(Q(name__icontains=query) | Q(email__contains=query))
        replayed(contacts, replayed)
    replayed(contacts)
    return render(request, 'contacts/list.html', {'contacts': contacts})


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
        contact_form = ContactReplayForm(request.POST or None, instance=contact)
        if request.method == 'POST':
            if contact_form.is_valid():
                contact_form.save()
            return redirect('contact:list')
        return render(request, 'contacts/edit.html', {'contact': contact, 'contact_form': contact_form})
