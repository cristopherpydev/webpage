from django.contrib import admin

from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
    list_filter = ('title','category')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
    list_filter = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}
