from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#응답을 주는 녀석 
def data(request):
    return HttpResponse('lunch time 배고파')

def lunch(request):
    return HttpResponse('lunch time 배고파')