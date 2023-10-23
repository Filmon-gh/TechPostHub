from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_profile_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.profile_picture.url')

    def get_is_profile_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

          
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_profile_owner', 'profile_id', 'profile_picture',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    
    post = serializers.ReadOnlyField(source='post.id')