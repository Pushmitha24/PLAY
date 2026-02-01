from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
user = User.objects.first()

from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import Post, Like, KarmaTransaction
from .serializers import PostSerializer
from .models import Post, Comment, Like, KarmaTransaction

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.prefetch_related(
            "comments",
            "comments__replies",
        )
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
@method_decorator(csrf_exempt, name="dispatch")
class LikePostView(APIView):
    @transaction.atomic
    def post(self, request, post_id):
        user = User.objects.first()  # 🔥 FIX

        post = get_object_or_404(Post, id=post_id)

        like, created = Like.objects.get_or_create(
            user=user,
            post=post
        )

        if created:
            KarmaTransaction.objects.create(
                user=post.author,
                points=5
            )

        return Response({"liked": created})

class LeaderboardView(APIView):
    def get(self, request):
        last_24h = timezone.now() - timedelta(hours=24)

        leaderboard = (
            KarmaTransaction.objects
            .filter(created_at__gte=last_24h)
            .values("user__username")
            .annotate(total_karma=Sum("points"))
            .order_by("-total_karma")[:5]
        )

        return Response(leaderboard)
@method_decorator(csrf_exempt, name="dispatch")
class LikeCommentView(APIView):
    @transaction.atomic
    def post(self, request, comment_id):
        user = User.objects.first()  # 🔥 FIX

        comment = get_object_or_404(Comment, id=comment_id)

        like, created = Like.objects.get_or_create(
            user=user,
            comment=comment
        )

        if created:
            KarmaTransaction.objects.create(
                user=comment.author,
                points=1
            )

        return Response({"liked": created})
