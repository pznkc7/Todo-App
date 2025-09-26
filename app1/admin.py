from django.contrib import admin
from .models import Todo

# Register your models here.

# admin.site.register(Todo)

@admin.register(Todo)
class DetailAdmin(admin.ModelAdmin):
    list_display=['id','task','created_at']