from django.shortcuts import render

from .models import Event


def home_page(request):
    data = Event.objects.filter(period__event__title='Старость')
    return render(request, 'views_works/home_page.html', {"data": data})


def childhood(request):
    data = Event.objects.filter(period__title="Детство")
    return render(request, 'views_works/childhood.html', {"data": data})


def youth(request):
    data = Event.objects.filter(period__title="Молодость")
    return render(request, 'views_works/youth.html', {"data": data})


def old_age(request):
    data = Event.objects.filter(period__title="Старость")
    return render(request, 'views_works/old_age.html', {"data": data})
