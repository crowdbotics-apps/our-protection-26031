from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, TaskViewSet, RatingViewSet, TaskTransactionViewSet

router = DefaultRouter()
router.register("tasktransaction", TaskTransactionViewSet)
router.register("message", MessageViewSet)
router.register("rating", RatingViewSet)
router.register("task", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
