from django.contrib import admin
from django.urls import path, include
from accounts.views import auth_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greencredit.urls')),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout')
]
