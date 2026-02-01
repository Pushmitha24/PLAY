from django.urls import path
from .views import PostListView, LikePostView, LeaderboardView,LikeCommentView
urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("posts/<int:post_id>/like/", LikePostView.as_view()),
    path("leaderboard/", LeaderboardView.as_view()),
    path("comments/<int:comment_id>/like/", LikeCommentView.as_view()),

]

