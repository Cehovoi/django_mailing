# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Subscriber, LetterInfo
from .tasks import run_mail


def index(request):
    context = get_context()
    return render(request, "index.html", context)


def send(request):
    run_mail.delay(check_url=request.build_absolute_uri('/opened/'))
    context = get_context()
    return render(request, "index.html", context)


def opened(request, letter_id):
    LetterInfo.objects.filter(pk=letter_id).update(opened=True)
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


