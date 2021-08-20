from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *                    

def index(request):
    # out task will take 10 sec in loading
    sleepy(10)

    # With the help of this we don't need to wait
    #sleepy.delay(10) 

    # send_mail_without_celery()
    return HttpResponse("<h1>Hello, Celery</h1>")