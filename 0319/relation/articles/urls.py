from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:id>/',views.article_detail),
    path('<int:id>/comments/', views.comment_list),
    path("<int:article_id>/comments/<int:comment_id>/", views.comment_detail),
    path('<int:article_id>/bookmarked_users/', views.bookmarked_user_list)
]
