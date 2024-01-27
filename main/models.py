from django.db import models


class Courses(models.Model):
    name_item = models.CharField(max_length=256)
    chapter = models.CharField(max_length=256, null=True, blank=True)
    subject = models.CharField(max_length=256)
    path_notes = models.TextField()
    path_video = models.TextField(blank=True, null=True)
