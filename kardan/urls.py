from django.contrib import admin
from django.urls import path, include
from karfarma import views
from karjoo.views import karjooregisterform
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('blog.urls')),
    path('karfarma/', include('karfarma.urls')),
    path('karjoo/', include('karjoo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
