#-*- coding: utf-8 -*-
import random
import simplejson as json
import codecs

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = 'index.html'

    return render(request, template)
