from django.contrib import admin
from django.urls import path
from app_wealthway import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.metas, name='metas'),
    path('', views.sucesso, name='sucesso'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)