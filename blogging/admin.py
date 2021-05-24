from django.contrib import admin
from blogging.models import Post, Category


class PostsInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author')
    exclude = ('created_date', 'modified_date', 'published_date')
    inlines = [
        PostsInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
