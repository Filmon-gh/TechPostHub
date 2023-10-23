from .serializers import PostSerializer
from rest_framework.views import APIView
from .models import Post
from rest_framework import status
from rest_framework.response import Response


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)