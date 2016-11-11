import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from json import dumps, loads, JSONEncoder, JSONDecoder
from django.forms.models import model_to_dict
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
        # serializer = PostSerializer(post, many=True)
        response = dict()
        response['id'] = post.id
        response['title'] = post.getTitle()
        response['text'] = post.getText()

        return HttpResponse(json.dumps(response))


class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
