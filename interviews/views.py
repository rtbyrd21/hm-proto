from django.shortcuts import render

from django.http import HttpResponse
import django_filters
from rest_framework import viewsets
from serializers import *
# from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RelatedImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = RelatedImagesSerializer

# class RelatedWomenViewSet(viewsets.ModelViewSet):
#     queryset = RelatedWomen.objects.all()
#     serializer_class = RelatedWomenSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Themes.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('theme',)


class ExcerptViewSet(viewsets.ModelViewSet):
    queryset = Excerpt.objects.all()
    serializer_class = ExcerptSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('themes__theme',)



class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = RelatedWomenSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

# class RelatedThemeViewSet(viewsets.ModelViewSet):
#     queryset = Themes.objects.all()
#     serializer_class = RelatedThemeSerializer


