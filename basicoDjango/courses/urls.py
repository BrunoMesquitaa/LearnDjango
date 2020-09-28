from django.urls import path
from courses.views import courses, detalhes


app_name='curso'
urlpatterns = [
    path('', courses, name="curso"),
    #path('<int:pk>/', detalhes, name="detalhes")
    path('<slug:title>/', detalhes, name="detalhes")
]