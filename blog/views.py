from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
# Create your views here.
from .models import Post

def blog_page(request):
    post_list = Post.objedts.all()
    return HttpResponse('hello!')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)