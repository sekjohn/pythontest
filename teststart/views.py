from .models import Post
from .Serializers import Postserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


# 클래식 베잇스 뷰(CBV)
class Postlist(APIView):
    
    
    def get(self, request, format= None):
        postquery = Post.objects.all()
        serializer = Postserializer(postquery, many=True)
        return Response(serializer.data)

        
    def post(self,request, format=None):
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

