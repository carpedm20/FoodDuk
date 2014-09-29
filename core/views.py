#-*- coding: utf-8 -*-
import random
import simplejson as json
import codecs
from mongoengine import connect, Document, DictField, ListField

from django.conf import settings
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect

from utils.func import *

connect('carpedm20')

class Movie(Document):
    info = DictField()
    tags = ListField(DictField())

def index(request):
    template = 'index.html'

    return render(request, template)
