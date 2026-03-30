from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.list_articles, name='list-articles'),
    path('article/<slug:article_slug>/', views.article_detail, name='article-detail'),
    path('category/<slug:category_slug>/',views.category_detail, name='category-detail'),
]
