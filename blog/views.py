import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from json import dumps, loads, JSONEncoder, JSONDecoder

from django.http import HttpResponse
# Create your views here.
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class blog_page(APIView):
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(id=request.GET['id']).first()
        response = dict()
        response['id'] = post.id
        response['title'] = post.getTitle()
        response['text'] = post.getText()
        return HttpResponse(json.dumps(response))

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        post = Post()
        post.author = request.user
        post.title = data.get('title')
        post.text = data.get('text')
        Post.publish(post)
        return HttpResponse(json.dumps(data))


class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
