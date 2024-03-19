from django.shortcuts import render
from django.http import HttpResponse

from .models import Article ,Comment
from .serializers import ArticleSerializer , CommentSerializer 

from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer

import logging#로고가 쌓일꺼야

logger = logging.getLogger(__name__)#로고가 쌓일꺼야

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # articles = Article.objects.filter(title='제목이야')
        serializer = ArticleSerializer(articles, many=True)
        
        logger.info("articles")#로고가 쌓일꺼야
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = request.user 
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(author = user)
            return Response(serializer.data, status=201)





@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = Article.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = ArticleSerializer(article, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204) # no content

@api_view(['POST']) #댓글 수정 
def comment_list(requests, id):
    data = requests.data
    article = Article.objects.get(id=id)
    serializer = CommentSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)

@api_view(['PUT','DELETE']) #댓글 업데이트, #삭제
def comment_detail(request, article_id, comment_id):
    if request.method == 'PUT':
        data = request.data
        comment = Comment.objects.get(id=comment_id)
        serializer = CommentSerializer(comment, data= data)
        if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    elif request.method == 'DELETE':
        comment= Comment.objects.get(id=comment_id)
        comment.delete()
        return Response(status=204)

@api_view(['GET'])    
def bookmarked_user_list(request, article_id):
    article = Article.objects.get(id=article_id)
    users = article.bookmark_users.all()

    serializer = UserSerializer(users, many =True)
    return Response(serializer.data)