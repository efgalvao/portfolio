from django.contrib import admin
from django.urls import path, include
from portfolio.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("portfolio/", include("portfolio.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
