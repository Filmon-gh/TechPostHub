from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.profile_picture.url')
    is_profile_owner = serializers.SerializerMethodField()

    def get_is_profile_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = ('id', 'owner', 'title', 'content', 'created_at', 'updated_at', 'is_profile_owner', 'profile_id', 'profile_picture')
      
