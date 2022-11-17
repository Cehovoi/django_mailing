from __future__ import absolute_import
from datetime import datetime

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from celery.schedules import crontab
from celery.task import periodic_task
from celery import shared_task

from .models import Subscriber, LetterInfo
from . import TEST_DOMAIN


def _run_mail():
    check_url = TEST_DOMAIN + '/opened/'
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
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


@shared_task()
def run_mail():
    _run_mail()


@periodic_task(run_every=(crontab(minute='*/2')),
               name="Dispatch_scheduled_mail",
               reject_on_worker_lost=True,
               ignore_result=True)
def run_schedule_mail():
    _run_mail()
