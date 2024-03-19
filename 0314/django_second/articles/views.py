from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Article

def sleepy(request):

    return HttpResponse("식곤증 온다,, ")

def articles(request):

    return HttpResponse("게시글")

def json_data(request):
    data = {'title' : '제목',
            'content' : '내용'}

    return JsonResponse(data)

#변수 만들기 위해서
def random_data(request, num):
    
    return HttpResponse(num)

def name(request, name):
    name_data = {name : '천재'}
    return JsonResponse(name_data)

def create(request):
    article = Article(
    title = '이거 제목임',
    content = '이거 내용임 '
    )
    
    article.save()

    return HttpResponse(article)

def read(request):
    articles = Article.objects.all()
    return HttpResponse(articles)

def read_single(request, id):
    article = Article.objects.get(id=id)
    return HttpResponse(article)