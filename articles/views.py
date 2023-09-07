from django.shortcuts import render
from .models import CategoryModel, ArticleModel

def home(request):
    context = {}
    categories = CategoryModel.objects.order_by('category_name')
    context['categories']= categories

    for category in categories:
        top_articles = ArticleModel.objects.filter(category=category).order_by('-rating')[:3]
        context[category.slug] = top_articles
    return render(request, 'index.html', context)



def category(request):
    context = {}
    categories = CategoryModel.objects.all()
    context['categories']= categories
    return render(request, 'articles/category.html', context)

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
    categories = CategoryModel.objects.order_by('category_name')
    context['categories']= categories
    for category in categories:
        top_articles = ArticleModel.objects.order_by('-rating').filter(category=category)
        context[category.slug] = top_articles
    return render(request, 'articles/article_details.html', context)
