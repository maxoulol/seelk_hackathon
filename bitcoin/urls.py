from django.urls import path
from bitcoin import views

urlpatterns = [
        path('bitcoin/', views.get_bitcoin_value),
        ]
