from rest_framework import serializers

from articles.models import Article as ArticleModel, Comment as CommentModel
from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = ArticleModel
        fields = "__all__"

# 방법1
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= CommentModel
#         fields="__all__"

# 방법2
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= CommentModel
#         fields="__all__"
#         extra_kwargs = {"article": {"read_only": True}, "user": {"read_only": True}}


# 방법3 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= CommentModel
        fields="__all__"