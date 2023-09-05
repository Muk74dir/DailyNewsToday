from django.shortcuts import render
from .models import CategoryModel, ArticleModel

def article(request):
    articles = ArticleModel.objects.all()
    return render(request, 'index.html', {'articles': articles})

def category(request):
    categories = CategoryModel.objects.all()
    articles = ArticleModel.objects.filter(rating="4")
    latest_articles = ArticleModel.objects.get(category='Latest')
    top_rated_article = ArticleModel.objects.get(rating='0')
    relavent_news = ArticleModel.objects.filter(category='Sports')
    print(relavent_news)
    return render(request, 'articles/category.html', {
        'articles': articles, 'categories': categories, 
        'latest_articles': latest_articles,
        'top_rated_article': top_rated_article,
        'relavent_news': relavent_news
        })

def article_by_category(request, category_slug):
    context = {}
    all_categories = CategoryModel.objects.all()
    category = CategoryModel.objects.get(slug=category_slug)
    categories = CategoryModel.objects.filter(slug=category_slug)
    articles = ArticleModel.objects.filter(category=category)
    context['category']= category
    context['categories']= categories
    context['articles']= articles
    context['all_categories']= all_categories
    return render(request, 'articles/category_details.html', context)

def article_details(request, category_slug, article_slug):
    context = {}
    article = ArticleModel.objects.get(slug=article_slug)
    context['article']= article
    return render(request, 'articles/article_details.html', context)
