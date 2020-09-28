from django import forms
from django.core.mail import send_mail
from django.conf import settings

from courses.mail import send_mail_teamplate

class ContactCourse(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    email = forms.EmailField(label="E-Mail")
    mensagem = forms.CharField(label="Mensagem",widget=forms.Textarea,required=False)

    def send_mail(self,course):
        subject = 'Contato sobre o Curso %s' % course
        #mensagem = 'Nome: %(name)s;E-mail: %(email)s;%(mensagem)s'
        contexto = {
            'name':self.cleaned_data['nome'],
            'email':self.cleaned_data['email'],
            'mensagem':self.cleaned_data['mensagem']
        }
        # mensagem = mensagem %contexto
        # send_mail(subject, mensagem, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

        send_mail_teamplate(subject, 'email_template.html', contexto, [settings.CONTACT_EMAIL])