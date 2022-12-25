from rest_framework import serializers
from rest_framework.schemas.openapi import AutoSchema

class CommentSerializer(serializers.Serializer, AutoSchema):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
