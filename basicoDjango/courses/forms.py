from django import forms

class ContactCourse(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    email = forms.EmailField(label="E-Mail")
    mensagem = forms.CharField(label="Mensagem",widget=forms.Textarea,required=False)
