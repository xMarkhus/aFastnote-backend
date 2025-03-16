from django.contrib.auth.models import User
from rest_framework import serializers
import re


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "confirm_password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True},
        }

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user

    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "O nome de usuário deve ter pelo menos 8 caracteres.")
        return value

    def validate_password(self, value):
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r"\d", value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos um número.")
        if not re.search(r"[!@#$%^&*()_+[\]{}|;:,.<>?]", value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos um caractere especial.")

        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                "As senhas devem ser iguais. Confirme a senha.")

        return attrs
