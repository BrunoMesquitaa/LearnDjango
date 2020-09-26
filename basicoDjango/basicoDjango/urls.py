from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='coracao')),
    path('cursos/', include('courses.urls',namespace='curso'))
]

#imagens
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
