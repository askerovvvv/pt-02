from rest_framework import serializers

from app.models import GameInformation, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "full_name"]


class GameInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = GameInformation
        fields = "__all__"

    def create(self, validated_data):
        return GameInformation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance



class TestSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

