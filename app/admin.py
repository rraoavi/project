from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content1','content2','content3','content4','content5','content6','content7','content8','image' ,'date_created')
    search_fields = ['title','content1','content2','content3','content1','content5','content1','content7','content8','image' , 'date_created']

