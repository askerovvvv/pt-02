from rest_framework import serializers

from account.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=3)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")

        if password2 != password:
            raise serializers.ValidationError("Пароли не совпадают!")

        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
