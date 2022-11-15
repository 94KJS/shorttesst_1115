from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.serializers import ArticleSerializer, CommentSerializer
from articles.models import Article as ArticleModel, Comment as CommentModel

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "로그인 해주세요"}, 401)

        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "글 작성 완료!!"})
        else:
            return Response({"message": f"${serializer.errors}"}, 400)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = ArticleModel.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CommentView(APIView):
    # 방법1
    # def post(self, request, pk):
    #     request.data._mutable = True
    #     request.data["user"] = request.user.id
    #     request.data["article"] = pk
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

    #     return Response({"message":serializer.errors})

    # 방법2
    # def post(self, request, pk):
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(article=ArticleModel.objects.get(pk=pk), user=request.user)
    #         return Response(serializer.data)

    #     return Response({"message":serializer.errors})

    # 방법3
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"message":serializer.errors})