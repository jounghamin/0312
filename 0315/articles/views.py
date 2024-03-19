from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Article
from .serializers import ArticleSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def article_list (request):
    if request.method == 'GET':  
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data = data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status =201)


@api_view(['GET', 'PUT','DELETE']) 
def article_detail(request,id):
    if request.method == 'GET':
        article = Article.objects.get(id = id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = Article.objects.get(id=id) #어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = ArticleSerializer(article, data=data, partial=True) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return  Response(status = 204) # no content 

# #생성 은 아티클에 대한 모델에 istanc 를 생성하는 것 
# article = Article(title = '제목이야', content = '글이야') 
# article.save()

# #조회 
# articles = Article.objects.all() #전체 조회 
# article = Article.objects.get(id=10) #id 가 10인 게시글 조회 

# articles = article.objects.filter(title='제목') 