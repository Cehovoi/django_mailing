# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Subscriber
from django.http import HttpResponse


def index(request):
    context = get_context()
    return render(request, "index.html", context)


def send(request):
    run_mail()
    context = get_context()
    return render(request, "index.html", context)


def check(request):
    context = get_context()
    return render(request, "index.html", context)


def get_context():
    subscribers = tuple((subscriber, subscriber.letterinfo_set.all())
                        for subscriber in Subscriber.objects.all()
                        )
    context = {'subscribers': subscribers,
               'amount_subscribers': len(subscribers),
               }
    return context


def run_mail():
    # there will bee celery connect
    #subscribers = Subscriber.objects.all()
    subscribers = Subscriber.objects.filter(id=10)
    for subscriber in subscribers:
        subscriber.letterinfo_set.create(sent=datetime.now())
        context = {'first_name': subscriber.first_name,
                   'last_name': subscriber.last_name,
                   'birth_date': subscriber.birth_date,
                   }
        html_message = render_to_string('mail.html', {'context': context})
