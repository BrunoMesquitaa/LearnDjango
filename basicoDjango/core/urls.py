from django.urls import path, re_path
from core.views import home,base,contato

urlpatterns = [
    path('teste/',home),
    re_path(r'^$',base, name='base'),
    re_path(r'^contato/$',contato, name='contact'),
]
