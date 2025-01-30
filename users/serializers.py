from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['password'] = user.password
        token['email'] = user.email

        return token
