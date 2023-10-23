from .serializers import PostSerializer
from rest_framework.views import APIView
from .models import Post
from rest_framework import status
from rest_framework.response import Response


class PostListView(APIView):
    serializer_class = PostSerializer
    

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Assign the owner based on the requesting user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    """
