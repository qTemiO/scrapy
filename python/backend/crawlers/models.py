from django.contrib.postgres.fields import ArrayField
from django.db import models


class HabrModel(models.Model):
    link = models.URLField(unique=True)
    title = models.TextField()
    posted = models.DateTimeField()
    tags = ArrayField(
            models.CharField(max_length=30, blank=True),
            blank=True, null=True
        )

    likes = ArrayField(
            models.IntegerField(blank=True),
            size=10, blank=True, null=True,
            default = list()
        )
    bookmarks = ArrayField(
            models.IntegerField(blank=True),
            size=10, blank=True, null=True,
            default = list()
        )
    views = ArrayField(
            models.IntegerField(blank=True),
            size=10, blank=True, null=True,
            default = list()
        )
    comments = ArrayField(
            models.IntegerField(blank=True),
            size=10, blank=True, null=True,
            default = list()
        )
    datetime = ArrayField(
            models.DateTimeField(),
            size=10, blank=True, null=True,
            default = list()
        )

    def __repr__(self):
        return f"{self.id}: {self.link}"
    
    def __str__(self):
        return f"{self.id}: {self.link}"