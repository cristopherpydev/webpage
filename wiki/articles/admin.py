from django.contrib import admin

from .models import Article, Category, Campaign, Character

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

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'state', 'description','type')
    search_fields = ('title', 'genre', 'state', 'type')
    list_filter = ('genre', 'state', 'type')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'biography')
    search_fields =('name', 'campaign')
    list_filter = ('name', 'campaign')
