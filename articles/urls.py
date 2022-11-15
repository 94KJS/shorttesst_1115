from django.urls import path
from articles import views


urlpatterns = [
    # user/
    path("", views.ArticleView.as_view(), name="article_view"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail_view"),
    path("<int:pk>/comment/", views.CommentView.as_view(), name="comment_view"),
]
