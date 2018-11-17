"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from banner.views import (
			BannerCreateView,
			InstallmentCreateView,
			BannerListView, 
			BannerDetailView,
			BannerUpdateView,
			InstallmentUpdateView,
			BannerDeleteView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BannerListView.as_view(), name='home'),
    path('create-banner',BannerCreateView.as_view(), name='create-banner'),
    path('create-installment',InstallmentCreateView.as_view(), name='create-installment'),
    path('update-banner/<str:slug>',BannerUpdateView.as_view(), name='update-banner'),
    path('update-installment/<int:pk>',InstallmentUpdateView.as_view(), name='update-installment'),
    path('<str:slug>',BannerDetailView.as_view(), name='detail'),
    path('<str:slug>/delete',BannerDeleteView.as_view(), name='delete-banner'),
    
    path('about', TemplateView.as_view(template_name="about.html")),
    path('contact', TemplateView.as_view(template_name="contact.html")),
]
