from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_custom, name="login_custom"),
    path("register/", views.register, name="register"),
    path("main/", views.main, name="main"),
    path('logout/', views.logout_view, name='logout'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:pk>/', views.campaign, name='campaign'),
    path('campaign/<int:pk>/get-businesses/', views.get_businesses, name='get_businesses'),
   # path('campaign/<int:pk>/generate-emails/', views.generate_emails, name='generate_emails'),
    path('testAPI/', views.testAPI, name='testAPI'),

]