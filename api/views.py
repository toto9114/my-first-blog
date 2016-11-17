from django.shortcuts import render
from rest_framework import viewsets
from models import Contents, Folders, Favors, Groups, Users
from serializers import ContentsSerializer, FoldersSerializer, FavorsSerializer
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly


# Create your views here.


class ContentsViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class FoldersViewSet(viewsets.ModelViewSet):
    queryset = Folders.objects.all()
    serializer_class = FoldersSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)


class FavorViewSet(viewsets.ModelViewSet):
    queryset = Favors.objects.all()
    serializer_class = FavorsSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = FavorsSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = FavorsSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)
