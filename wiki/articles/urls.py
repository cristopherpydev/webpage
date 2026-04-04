from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.list_articles, name='list-articles'),
    path('article/<slug:article_slug>/', views.article_detail, name='article-detail'),
    path('category/<slug:category_slug>/',views.category_home_detail, name='category-detail'),
    path('categories/',views.list_categories),
    path('campaign/<slug:campaign_slug>/', views.campaign_detail, name='campaign-detail'),
    path('campaigns/', views.list_campaigns),
    path('articles/article/', views.list_articles),
    path('campaign/<slug:campaign_slug>/category/<slug:category_slug>/',views.category_detail, name='campaign-category-detail'
)
]
