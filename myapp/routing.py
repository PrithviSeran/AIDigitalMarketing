from django.urls import path

from .consumers import WSConsumer, CampaignWSConsumer


ws_urlpatterns = [
    path('ws/ok/', WSConsumer.as_asgi()),
    path('ws/campaigns/', CampaignWSConsumer.as_asgi())
]