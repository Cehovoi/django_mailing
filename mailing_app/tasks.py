from __future__ import absolute_import
from datetime import datetime
from time import sleep
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task

from .models import Subscriber, LetterInfo


@shared_task()
def run_mail(check_url=None):
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        sleep(2)
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
        plain_message = strip_tags(html_message)
        from_email = ''
        to = subscriber.email
        send_mail(subject, plain_message, from_email, [to],
                  html_message=html_message)
