from users.apps import UsersConfig
from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(), name="Payments_list")
]

urlpatterns += router.urls
