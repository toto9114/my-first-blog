from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Contents(models.Model):
    content_body = models.TextField()
    morpheme = models.TextField()
    content_scored = models.TextField()
    admin_delete = models.BooleanField(default=False)


class Folders(models.Model):
    folder_contents = models.TextField()
    related_group = models.TextField()
    admin_dislike = models.BooleanField()


class Favors(models.Model):
    favor = models.IntegerField()


class Groups(models.Model):
    current_group_favor = models.IntegerField()
    curation_folder = models.IntegerField()
    future_possible_group = models.IntegerField()
    past_group_favor = models.IntegerField()

class Users(models.Model):
    user_group = models.IntegerField()
    current_user_favor = models.IntegerField()
    curation_folder = models.IntegerField()
    past_user_group = models.IntegerField()
    past_user_favor = models.IntegerField()
