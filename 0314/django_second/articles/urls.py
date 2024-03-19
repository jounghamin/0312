from django.urls import path 
from articles import views
from . import views 
# from .models import Article

#일반적 
# urlpatterns = [

#     path('articles/',views.articles),
#     path('articles/json-data', views.json_data)
# ]

#변수로 만든다 url에 숫자를 받는 것 
urlpatterns = [
    path('',views.articles),
    # path('articles/json-data', views.json_data),
    # path('random-data/<int:num>/', views.random_data),
    path("json-data/", views.json_data),
    path('name/<str:name>/', views.name),
    path('create/', views.create),
    path('read/', views.read),
    path('read/<int:id>/' ,views.read_single)
    ]




