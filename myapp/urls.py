from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login_custom, name='login_custom'),
    path("register/", views.register, name="register"),
    path("main/", views.main, name="main"),
    path('logout/', views.logout_view, name='logout'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:id>/', views.campaign, name='campaign'),
    path('domain/<int:id>/<int:campaign_id>', views.domain, name='domain'),
    path('generate_email/<int:id>/<int:campaign_id>/<str:email_to>', views.generate_email, name='generate_email'),
]