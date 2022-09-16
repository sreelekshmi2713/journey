
from os import path

from django.contrib import admin
import django.urls
from django.urls import include

from travelproject import settings
from django.conf.urls.static import static

urlpatterns = [
    django.urls.path('admin/', admin.site.urls),
    django.urls.path('', include('travelapp.urls')),
    django.urls.path('hope/', include('hope.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
