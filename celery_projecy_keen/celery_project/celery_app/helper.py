from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('CELERY WORKED YEAH', 'CELERY IS COOL',
              'abhirvalandge@gmail.com',
              ['abhirva.landge@echelonedge.com'],
              fail_silently=False
              )
    return None