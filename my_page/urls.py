from django.urls import path
from . import views
from .views import CustomAuthToken

app_name = 'my_page'

urlpatterns = [
    path('', views.MyBlog.as_view(), name='my_blog'),
    path('api-token-auth/', CustomAuthToken.as_view())
    # Add more paths here
]