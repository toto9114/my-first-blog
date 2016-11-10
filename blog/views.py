import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from json import dumps, loads, JSONEncoder, JSONDecoder
from django.forms.models import model_to_dict
from django.http import JsonResponse
# Create your views here.
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class blog_page(APIView):

    def get(self, request, fromat=None):
        post = Post.objects.filter(id=1).first()
        # serializer = PostSerializer(post, many=True)
        post_dict = model_to_dict(post)

        return JsonResponse(post_dict, safe=False).content


class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
