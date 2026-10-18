from django.contrib import admin
from .models import Section, Part, Delivery, Expense

admin.site.register(Section)
admin.site.register(Part)
admin.site.register(Delivery)
admin.site.register(Expense)
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')