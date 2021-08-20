from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duartion):
    sleep(duartion)
    return None

@shared_task
def send_mail_task():
    send_mail('CELERY WORKED YEAH', 'CELERY IS COOL',
              'abhirvalandge@gmail.com'
              ['abhirva.landge@echelonedge.com'],
              fail_silently=False
              )
    return None