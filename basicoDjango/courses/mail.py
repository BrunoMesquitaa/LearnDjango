from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail_teamplate(subject, template, contexto, recipient,
                        from_email = settings.DEFAULT_FROM_EMAIL, fail_silently = False):
    
    mensagem_html = render_to_string(template,contexto)
    mensagem_text = striptags(mensagem_html)

    email = EmailMultiAlternatives(subject = subject, body = mensagem_text,
                                   from_email = from_email, to = recipient)
    
    email.attach_alternative(mensagem_html,'text/html')
    email.send(fail_silently=fail_silently)