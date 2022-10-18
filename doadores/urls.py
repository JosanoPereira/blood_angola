from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('doador/', include('apps.doador.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('familiar/', include('apps.familiar.urls')),
    path('hospital/', include('apps.hospital.urls')),
    path('tipo_sangue/', include('apps.tipo_sangue.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
