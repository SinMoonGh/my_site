from rest_framework import serializers
from .models import Album, Photo

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'description']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'description', 'image', 'upload_dt']