# polls 폴더에 urls.py가 업어서 새로 생성

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PhotoViewSet

app_name = "photo"

router = DefaultRouter()
router.register(r"album", AlbumViewSet)
router.register(r"photo", PhotoViewSet)

urlpatterns = [    
    path("", views.AlbumLV.as_view(), name="index"),
    path("album", views.AlbumLV.as_view(), name="album_list"),
    path("album/<int:pk>", views.AlbumDV.as_view(), name="album_detail"),
    path("photo/<int:pk>", views.PhotoDV.as_view(), name="photo_detail"),
    path('', include(router.urls)),
]