from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'order', 'created_at')
