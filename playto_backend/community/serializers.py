from rest_framework import serializers
from .models import Post, Comment


class RecursiveCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at", "replies"]

    def get_replies(self, obj):
        children = obj.replies.all()
        return RecursiveCommentSerializer(children, many=True).data


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at", "comments"]

    def get_comments(self, obj):
        root_comments = obj.comments.filter(parent__isnull=True)
        return RecursiveCommentSerializer(root_comments, many=True).data
