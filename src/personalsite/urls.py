"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from landingpage.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', display_html, name="display_html"),
    path('admin/', admin.site.urls),
    path('projects/loan_calc/', include('loan_calc.urls')),
    path('projects/weather/', include('weather.urls')),
    path('projects/newsreader/', include('newsreader.urls')),
    path('blog/', display_blog, name="display_blog"),
    path('contacted/', contacted, name="contacted"),
    path('sitemap', sitemap, name="sitemap"),
    path('privacy', privacy, name="privacy"),
    path('projects', project, name="project"),
    path('product/<slug>', product_view, name="product_view"),
    path('cart/<pk>', Push_to_cart, name="Push_to_cart"),
    path('cart/', Cart_view, name="Cart_view"),
] 
