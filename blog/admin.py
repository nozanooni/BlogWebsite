
from django.contrib import admin
from .models import User, Post, Comment, Category


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_published')
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'content', 'date_posted')
admin.site.register(Comment, CommentAdmin)


admin.site.register(Category)



