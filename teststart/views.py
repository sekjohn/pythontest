from .models import Post
from .Serializers import Postserializer
from rest_framework.viewsets import ModelViewSet

# 클래식 베잇스 뷰(CBV)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_calss = Postserializer    

