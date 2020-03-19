from django.contrib import admin
# Register your models here.
from .models import Post, Comment, Postlike

class PostInstanceInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    inlines = [PostInstanceInline]
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body',)

admin.site.register(Comment, CommentAdmin)


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_name', 'post_likes')
    search_fields = ('name',)

admin.site.register(Postlike, PostLikeAdmin)