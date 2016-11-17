from .models import Contents, Folders, Favors, Groups, Users
from rest_framework import serializers


class ContentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contents
        fields = {'id', 'content_body', 'morpheme', 'content_scored', 'admin_delete'}


class FoldersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folders
        fields = {'id', 'folder_contents', 'related_group', 'admin_dislike'}


class FavorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favors
        fields = {'favor'}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = {'user_group', 'current_user_favor','curation_folder','past_user_group','past_user_favor'}


class GroupSerializer(serializers.ModelSerializer):
    group_users = Users.objects.all()

    class Meta:
        model = Groups
        fields = {'id', 'group_users', 'current_group_favor', 'curation_folder', 'future_possible_group', 'past_group_favor'}