# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.CharField(max_length=20,
                             db_index=True,
                             default='zhenyha.vo@gmail.com'
                             )

    def __str__(self):
        return '%s %s %s %s,\n' % (self.first_name,
                                   self.last_name,
                                   self.birth_date,
                                   self.email,
                                   )


class LetterInfo(models.Model):
    sent = models.DateTimeField()
    opened = models.BooleanField(default=False)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return 'sent - %s,  opened - %s' % (self.sent, self.opened)


def db_filler(amount_subscribers=3):
    from datetime import date
    from random import choice
    import names
    birth_years = range(1922, 2023)
    birth_months = range(1, 13)
    birth_days = range(1, 31)
    for _ in range(amount_subscribers):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        birth_date = (date(choice(birth_years),
                           choice(birth_months),
                           choice(birth_days)
                           )
                      )
        subscriber = Subscriber(first_name=first_name,
                                last_name=last_name,
                                birth_date=birth_date,
                                )
        subscriber.save()
