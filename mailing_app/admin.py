# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subscriber, LetterInfo


admin.site.register(Subscriber)
admin.site.register(LetterInfo)
