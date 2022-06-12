# config/urls.py

from django.contrib import admin
from django.urls import path, include

app_name="portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
