from django.contrib import admin
from django.urls import path, include

from tiktok import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    # path('merchants/', include('Merchant_Management.urls')),
]
