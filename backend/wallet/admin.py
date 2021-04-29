from django.contrib import admin
from .models import (
    PaymentTransaction,
    PaymentMethod,
    TaskerWallet,
    TaskerPaymentAccount,
    CustomerWallet,
)

admin.site.register(TaskerWallet)
admin.site.register(CustomerWallet)
admin.site.register(TaskerPaymentAccount)
admin.site.register(PaymentMethod)
admin.site.register(PaymentTransaction)

# Register your models here.
