from django.urls import path, include

from .views import PaymentView, PaymentCallbackView


urlpatterns = [
    path('', PaymentView.as_view(), name='payment'),
    path('callback/', PaymentCallbackView.as_view(), name='payment_callback'),
]
