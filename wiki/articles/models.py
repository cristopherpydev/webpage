from django.db import models

# Create your models here.
class Category(models.Model):
    '''Category class for the database mapping'''
    category_name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, null=True)    
    def __str__(self):
        return self.category_name
    
#1tomany relationship    
class Article(models.Model):
    '''Article class for the database mapping'''
    title = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.SlugField(null=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


