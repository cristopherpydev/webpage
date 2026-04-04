from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Article, Category, Campaign

def list_articles(request):
    '''we render here all the articles'''
    articles = Article.objects.all()
    return render(request, 'documents/articles.html', {'articles': articles})

def article_detail(request, article_slug:str):
    try:
        article = Article.objects.get(slug=article_slug)
        category = article.category
    except Article.DoesNotExist:
        return HttpResponse(f"This does not exists.")
    return render(request, 'documents/article.html', {'article':article, 'category':category})

def list_categories(request):
    '''rendering all categories'''
    categories = Category.objects.all()
    return render(request, 'documents/categories.html', {'categories':categories})

def category_home_detail(request, category_slug:str):
    category = Category.objects.get(slug=category_slug)    
    articles = Article.objects.filter(category=category)    
    return render(request, 'documents/category.html', {'category':category, 'articles':articles})
def list_campaigns(request):
    campaigns = Campaign.objects.all()
    return render(request, 'documents/campaign-historic.html', {'campaigns':campaigns})
def campaign_detail(request, campaign_slug:str):
    campaign = Campaign.objects.get(slug=campaign_slug)
    return render(request, 'documents/campaign.html', {'campaign':campaign})
def category_detail(request, campaign_slug: str, category_slug: str):
    campaign = Campaign.objects.get(slug=campaign_slug)
    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(category=category, campaign=campaign)
    return render(request,'documents/category.html', {'campaign': campaign,'category': category, 'articles': articles}
    )