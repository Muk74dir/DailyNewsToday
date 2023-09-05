from django.contrib import admin

from .models import CategoryModel, ArticleModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'description')
    prepopulated_fields = {'slug': ('category_name',)}
    ordering = ['category_name']


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'slug', 'category', 'rating', 'publishing_date')
    prepopulated_fields = {'slug': ('headline',)}
    ordering = ['-rating']
