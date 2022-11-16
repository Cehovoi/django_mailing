# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Subscriber
from django.http import HttpResponse


def index(request):
    context = {'amount_subscribers': Subscriber.objects.count()}
    return render(request, "index.html", context)


def send(request):
    # return HttpResponse('In SEND')
    return render(request, "index.html",)


def check(request):
    subscribers = Subscriber.objects
    context = {'subscribers': subscribers.all(),
               'amount_subscribers': subscribers.count()}
    return render(request, "index.html", context)
