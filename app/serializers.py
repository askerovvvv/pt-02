from rest_framework import serializers

from app.models import GameInformation


class GameInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    version = serializers.IntegerField()
    date_issue = serializers.DateField()
    company_name = serializers.CharField(max_length=50)
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return GameInformation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance




