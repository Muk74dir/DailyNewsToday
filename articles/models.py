from django.db import models
from .constants import CATEGORY, RATING

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=20, choices=CATEGORY)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/images', null=True, blank=True)

    def __str__(self):
        return self.category_name


class ArticleModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='articles')
    slug = models.SlugField(max_length=20, unique=True)
    headline = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY)
    image = models.ImageField(upload_to='articles/images')
    rating = models.CharField(max_length=10, choices=RATING)
    publishing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline