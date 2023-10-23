from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_info= serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.profile.profile_picture.url')

    def get_profile_infor(self, obj):
        request = self.context['request']
        return request.user == obj.owner

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('id', 'owner', 'title', 'content', 'created_at', 'updated_at', 'profile_info', 'profile_id', 'profile_picture')

      
