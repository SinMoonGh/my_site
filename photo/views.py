from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Photo
from rest_framework import viewsets
from .serializers import AlbumSerializer, PhotoSerializer
# Create your views here.

class AlbumLV(ListView):
    model=Album
    

class AlbumDV(DetailView):
    model=Album
    template_name='photo/album_detail.html'
    # pk를 통해서 특정 앨범만 가져온다

class PhotoDV(DetailView):
    model=Photo
    template_name='photo/photo_detail.html'


# ViewSets define the view behavior.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer