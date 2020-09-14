from .models import Post
from .Serializers import Postserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics 


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer


# 클래식 베잇스 뷰(CBV)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

