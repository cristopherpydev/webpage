from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article, Category, Campaign
def salute(request):
    return HttpResponse("Hello, this is a test")

def homepage(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    campaigns = Campaign.objects.all()
    articles = articles[:5]
    return render(request, 'documents/index.html', {'articles':articles, 'categories':categories, 'campaigns':campaigns})
