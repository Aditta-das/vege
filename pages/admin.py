from django.contrib import admin
from .models import Detail, Comment

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_stock', 'price')
    list_display_links = ('id', 'title')

admin.site.register(Detail, Admin)

admin.site.register(Comment)
