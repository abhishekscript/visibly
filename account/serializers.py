from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # mark email unique since no restriction exists by default
    User._meta.get_field('email')._unique = True
    class Meta:
        model = User
        fields = (
            'username', 'last_name', 'first_name', 'email', 'password'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False}
        }

    def create(self, validated_data):
        
        # validated_data contains {'email': <str>, 'username': <str>}
        # double ** converts dictionary into params, ex: User(email=<str>, username=<str>)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data['email']
        user.set_password(password)
        user.save()
        return user
