from django.contrib import admin

# Register your models here.
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'is_published',)
    list_display_links = ('title', 'id')
    search_fields = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ()
    list_filter = ()
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
