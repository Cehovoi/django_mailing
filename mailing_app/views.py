# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Subscriber, LetterInfo


def index(request):
    context = get_context()
    return render(request, "index.html", context)


def send(request):
    run_mail(check_url=request.build_absolute_uri('/opened/'))
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


def run_mail(check_url=None):
    # there will bee celery connect
    subscribers = Subscriber.objects.all()
    #subscribers = Subscriber.objects.filter(id=10)
    for subscriber in subscribers:
        # subscriber.letterinfo_set.create(sent=datetime.now())
        letter_info = LetterInfo(sent=datetime.now(), subscriber=subscriber)
        letter_info.save()
        image_url = '%s%s' % (check_url, letter_info.id)
        context = {'first_name': subscriber.first_name,
                   'last_name': subscriber.last_name,
                   'birth_date': subscriber.birth_date,
                   'image_url': image_url
                   }
        subject = 'Subject'
        html_message = render_to_string('mail.html', context)
        plain_message = strip_tags(html_message)  # ??
        from_email = ''
        to = subscriber.email
        mail.send_mail(subject, 'plain_message', from_email, [to],
                       html_message=html_message)
