from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

class Location(models.Model):
    city = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.city

class Images(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    url = models.CharField(max_length=2000, null=True, blank=True)


class Themes(models.Model):
    theme = models.CharField(max_length=200)
    def __unicode__(self):
        return self.theme

    class Meta:
        ordering = ["theme"]
        verbose_name_plural = "themes"
#
# class PlaceCategory(models.Model):
#     type = models.CharField(max_length=128)
#     def __unicode__(self):
#         return self.type


class Excerpt(models.Model):
    extract = models.CharField(max_length=2000, null=True, blank=True)
    audio_url = models.IntegerField(null=True, blank=True)
    start_time = models.IntegerField(null=True, blank=True)
    end_time = models.IntegerField(null=True, blank=True)
    themes = models.ManyToManyField(Themes, blank=True)
    images = models.ManyToManyField(Images, blank=True)
    def __unicode__(self):
        return self.extract

    class Meta:
        ordering = ["extract"]



class Women(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, blank=True)
    excerpt = models.ManyToManyField(Excerpt, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "women"

    def __unicode__(self):
        return self.name
    