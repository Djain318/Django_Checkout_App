 # (We'll create this file manually)

from django.urls import path
from .views import CheckoutAPIView

urlpatterns = [
    path('checkout/', CheckoutAPIView.as_view(), name='checkout'),
]
