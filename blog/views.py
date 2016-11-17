import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from serializers import PostSerializer, UserSerializer
from rest_framework import generics
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.
from .models import Post
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
