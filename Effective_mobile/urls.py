from django.contrib import admin
from django.urls import path, include
from Effective_mobile import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tradeApp.urls')),
    path('app/', include('authorization.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
