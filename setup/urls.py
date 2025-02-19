from django.contrib import admin
from django.urls import path, include
from accounts.views import auth_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greencredit.urls')),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
