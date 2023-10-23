from rest_framework import generics, permissions
from techhabpost.permissions import IsOwnerOrCustomPermission
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentListView(generics.ListCreateAPIView):
    
    serializer_class = CommentSerializer
    access_permissions = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):

    access_permissions = [IsOwnerOrCustomPermission]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


   