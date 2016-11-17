from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('owner', 'id', 'title', 'text', 'created_date', 'published_date')


class UserSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'blog')
