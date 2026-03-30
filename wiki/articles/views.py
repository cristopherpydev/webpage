from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Article, Category

def list_articles(request):
    '''we render here all the articles'''
    articles = Article.objects.all()
    return render(request, 'documents/articles.html', {'articles': articles})

def article_detail(request, article_slug:str):
    try:
        article = Article.objects.get(slug=article_slug)
    except Article.DoesNotExist:
        return HttpResponse(f"This does not exists.")
    return render(request, 'documents/article.html', {'article':article})

def list_categories(request):
    '''rendering all categories'''
    categories = Category.objects.all()
    return render(request, 'documents/categories.html', {'categories':categories})
def category_detail(request, category_slug:str):
    category = Category.objects.get(slug=category_slug)    
    articles = Article.objects.filter(category=category)    
    return render(request, 'documents/category.html', {'category':category, 'articles':articles})
