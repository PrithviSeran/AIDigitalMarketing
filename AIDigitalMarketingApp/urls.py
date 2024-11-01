"""
URL configuration for AIDigitalMarketingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myapp.urls")),
    path("accounts/", include("allauth.urls")),
    path('wel/', ReactView.as_view(), name="something"),
    path('wel/login/', UserLogin.as_view(), name='login'),
    path('wel/main/', MainPage.as_view(), name='main'),
    path('wel/logout/', UserLogout.as_view(), name='logout'),
    path('wel/createcampaign/', CreateCampaign.as_view(), name='CreateCampaign'),
    path('wel/domains/', CampaignBusinesses.as_view(), name='Domains'),
    path('wel/getemailcontent/', GetEmailContent.as_view(), name='Email'),
    path('wel/getemail/', GetEmail.as_view(), name='Email'),
    path('wel/sendemail/', SendEmail.as_view(), name='SendEmail'),


]
