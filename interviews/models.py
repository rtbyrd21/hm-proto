from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

class Location(models.Model):
    city = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["city"]
        verbose_name_plural = "locations"

    def __unicode__(self):
        return self.city

class Images(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    url = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "images"

    def __unicode__(self):
        return self.title


class Themes(models.Model):
    theme = models.CharField(max_length=200)
    def __unicode__(self):
        return self.theme

    class Meta:
        ordering = ["theme"]
        verbose_name_plural = "themes"


class Women(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, blank=True)
    # excerpt = models.ManyToManyField(Excerpt, blank=True)

    class Meta:
        ordering = ["location", "name"]
        verbose_name_plural = "women"

    def __unicode__(self):
        return self.name + " | " + unicode(self.location)


class Excerpt(models.Model):
    women = models.ForeignKey(Women, null=True, blank=True)
    extract = models.CharField(max_length=2000, null=True, blank=True)
    audio_url = models.CharField(max_length=2000, null=True, blank=True)
    start_time = models.IntegerField(null=True, blank=True)
    end_time = models.IntegerField(null=True, blank=True)
    clip_number = models.IntegerField(default=1, null=True, blank=True)
    themes = models.ManyToManyField(Themes, blank=True)
    images = models.ManyToManyField(Images, blank=True)
    def __unicode__(self):
        return ''

    class Meta:
        ordering = ["extract"]




    