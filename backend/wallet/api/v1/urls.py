from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    PaymentMethodViewSet,
    TaskerWalletViewSet,
    TaskerPaymentAccountViewSet,
    CustomerWalletViewSet,
)

router = DefaultRouter()
router.register("taskerwallet", TaskerWalletViewSet)
router.register("customerwallet", CustomerWalletViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
