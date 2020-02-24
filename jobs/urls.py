from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from photos.views import PhotoView
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('photos/', PhotoView.as_view(), name='photos'),
    path('accounts/', include('accounts.urls')),
    path('api/', include([
        path('', include('jobsapp.api.urls')),
    ])),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
