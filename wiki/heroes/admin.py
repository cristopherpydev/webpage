from django.contrib import admin
from .models import Person
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'experience', 'dnd','pathfinder', 'cthulhu', 'indie', 'others', 'none', 'interests', 'modality', 'first_term', 'second_term')
    search_fields = ('mail','phone','modality')
    list_filter = ('mail','experience','modality')
