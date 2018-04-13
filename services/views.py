# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ServiceForm, SercicePostForm, ServicePriceForm
from .models import Service, ServicePost, ServicePrice


# Create your views here.
def service_list_create(request):
    services = Service.objects.all()
    service_form = ServiceForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and request.user.is_authenticated:
        if service_form.is_valid():
            service_form.save()
            return redirect('service:list_create')
    return render(request, 'services/service/list.html', {'services': services, 'service_form': service_form})


def service_detail_update(request, slug):
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all().exclude(slug=service.slug)
    service_form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
    post_form = SercicePostForm(request.POST or None, request.FILES or None)
    price_form = ServicePriceForm(request.POST or None)
    if request.method == 'POST' and request.user.is_authenticated:
        if service_form.is_valid():
            service_form.save()
            return redirect('/{}/services/{}/detail/'.format(request.LANGUAGE_CODE, service.slug))
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.service = service
            new_post.save()
            return redirect('/{}/services/{}/detail/'.format(request.LANGUAGE_CODE, service.slug))
        if price_form.is_valid():
            new_price = price_form.save(commit=False)
            new_price.service = service
            new_price.save()
            return redirect('/{}/services/{}/detail/'.format(request.LANGUAGE_CODE, service.slug))
    return render(request, 'services/service/detail.html', {'service': service,
                                                            'services': services,
                                                            'service_form': service_form,
                                                            'post_form': post_form,
                                                            'price_form': price_form})


@login_required
def service_delete(request, slug):
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.all()
    if request.method == 'POST' and request.user.is_authenticated:
        service.delete()
        return redirect('service:list_create')
    return render(request, 'services/service/delete.html', {'service': service, 'services': services})


def service_post_detail_update(request, post_slug, service_slug):
    service = get_object_or_404(Service, slug=service_slug)
    services = Service.objects.all()
    post = get_object_or_404(ServicePost, slug=post_slug)
    post_form = SercicePostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST' and request.user.is_authenticated:
        if post_form.is_valid():
            post_form.save()
            return redirect('/{}/post/{}/{}/detail'.format(request.LANGUAGE_CODE, service.slug, post.slug))
    return render(request, 'services/post/detail.html',
                  {'service': service, 'services': services, 'post': post, 'post_form': post_form})


@login_required
def service_post_delete(request, post_slug):
    post = get_object_or_404(ServicePost, slug=post_slug)
    services = Service.objects.all()
    if request.method == 'POST':
        post.delete()
        return redirect('/{}/services/{}/detail/'.format(request.LANGUAGE_CODE, post.service.slug))
    return render(request, 'services/post/delete.html', {'post': post, 'services': services})


def service_price_detail(request, slug):
    price = get_object_or_404(ServicePrice, slug=slug)
    services = Service.objects.all()
    other_prices = ServicePrice.objects.all().filter(service=price.service).exclude(slug=price.slug)
    price_form = ServicePriceForm(request.POST or None, instance=price)
    if request.method == 'POST' and request.user.is_authenticated:
        if price_form.is_valid():
            price_form.save()
            return redirect('/{}/price/{}/detail'.format(request.LANGUAGE_CODE, price.slug))
    return render(request, 'services/price/detail.html',
                  {'price': price, 'price_form': price_form, 'other_prices': other_prices, 'services': services})


@login_required
def service_price_delete(request, slug):
    price = get_object_or_404(ServicePrice, slug=slug)
    services = Service.objects.all()
    if request.method == 'POST':
        price.delete()
        return redirect('/{}/services/{}/detail/'.format(request.LANGUAGE_CODE, price.service.slug))
    return render(request, 'services/price/delete.html', {'price': price, 'services': services})
