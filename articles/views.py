from django.shortcuts import render, redirect, HttpResponse
from .models import CategoryModel, ArticleModel
from accounts.models import UserRegistrationModel
import math

def home(request):
    context = {}
    all_categories = CategoryModel.objects.all()
    context['all_categories']= all_categories
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
    rating = request.POST.get('rating')
    all_categories = CategoryModel.objects.all()
    context['all_categories'] = all_categories

    category = CategoryModel.objects.get(slug=category_slug)
    article = ArticleModel.objects.get(slug=article_slug)
    context['article']= article

    relavent_articles = ArticleModel.objects.filter(category=category).exclude(slug=article_slug)[:2]
    context['relavent_articles']= relavent_articles

    user = request.user
    if user.is_authenticated:
        account = UserRegistrationModel.objects.get(user=user)
        context['account'] =  account

    
    all_subscriber = UserRegistrationModel.objects.all().count()
    if rating is not None:
        article.rating = (int(rating)//(all_subscriber))
        article.save()
        context['article']= article
    return render(request, 'articles/article_details.html', context)


def delete(request, category_slug, article_slug):
    user = request.user
    if user.is_authenticated:
        user = UserRegistrationModel.objects.get(user=user)
        if user.account_type == 'Editor':
            article = ArticleModel.objects.get(slug=article_slug)
            article.delete()
        else:
            return HttpResponse('You are not Authorised ')
    else:
        return HttpResponse('You are not Authorised to do this')
    
    return redirect('home')