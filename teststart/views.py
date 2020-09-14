from .models import Post
from .Serializers import Postserializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PostListAPIView(APIView):
    def get(self, requset):
        post = Post.objects.all()
        postlistserializer = Postserializer(post, many=True)
        return Response(postlistserializer.data)
    def post(self, requset):
        postlistserializer = Postserializer(data=requset.data)
        if postlistserializer.is_valid():
            postlistserializer.save()
            return Response(postlistserializer.data, status=201)
        return Response(postlistserializer.erros, status=400)

class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = Postserializer(post)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = Postserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, statis=statis.HTTP_404_REQUSET)
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)