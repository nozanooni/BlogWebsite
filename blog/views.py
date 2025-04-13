from django.shortcuts import render
from .models import User, Post, Comment, Category

def main(request):
    return render(request, 'blog/main.html')

def master(request):
    return render(request, 'blog/master.html')

def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})


def comments(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})

def blogdetails(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/blogdetails.html', {'post': post})




