
from rest_framework import serializers
from user_app import models


class UserApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserApplication
        fields = '__all__'


class UserApplicationDeploymentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    app_id = serializers.IntegerField()
