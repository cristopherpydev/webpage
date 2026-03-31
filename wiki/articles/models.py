from django.db import models

# Create your models here.
class Category(models.Model):
    '''Category class for the database mapping'''
    category_name = models.CharField(max_length=32)
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
    

class Campaign(models.Model):
    '''Campaign class for the database mapping'''
    states = [('active', 'Active'), ('stopped', 'Stopped')]
    genres = [('high_fantasy', 'High Fantasy'), ('horror', 'Horror'), ('weird', 'Weird'), ('futuristic', 'Futuristic'), ('classic', 'Classic')]
    types = [('oneshot','Oneshot'), ('long_term_campaign', 'Long term campaign'), ('shortie', 'Short campaign')]
    
    
    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(Category, related_name='categories', blank=True)
    description = models.TextField()
    #CHOICES 
    state = models.CharField(choices=states, default='active')
    genre = models.CharField(choices=genres, default='classic')
    type = models.CharField(choices=types, default='long_term_campaign')
    def __str__(self):
        return self.title


class Character(models.Model):
    '''Character class for the database mapping'''
    name = models.CharField(max_length=64, blank=True)
    birth_date = models.DateField()
    biography = models.TextField()
    campaign = models.ManyToManyField(Campaign, related_name='campaigns', blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, default='character')
