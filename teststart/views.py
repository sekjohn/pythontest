from .models import Post
from .Serializers import Postserializer
from rest_framework.viewsets import ModelViewSet

# 클래식 베잇스 뷰(CBV)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body : ", request.body)
        print("request.body : ", request.body)
        return super().dispatch(request, *args, **kwargs)
    
