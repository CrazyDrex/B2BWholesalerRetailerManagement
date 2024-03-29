"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Abhishek Cars Admin"
admin.site.site_title = "Abhishek Cars Portal"
admin.site.index_title = "Welcome to Abhishek Cars"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('listings/',include('listings.urls')),
    path('acounts/',include('acounts.urls')),
    path('contact/',include('inquiry.urls')),



  

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
