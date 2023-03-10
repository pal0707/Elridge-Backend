from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Post, User



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'author']