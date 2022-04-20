import email
from email import message
from unicodedata import name
from django.shortcuts import render
from .models import Blog, Tag, Category, Comments
from .forms import CommentForm


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,'blogs/blog_list.html',context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blog=blog)
    recents = Blog.objects.all().order_by("-published_at")[:4]
    categories = Category.objects.all()
    comments = Comments.objects.filter(blog=blog)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]  
            new_message = form.cleaned_data ["message"] 
            
            new_comment = Comments(blog=blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()
            
    context = {
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments
    }
    return render(request,'blogs/blog_detail.html',context)


def blog_tag(request,tag):
    blogs = Blog.objects.filter(tag__slug=tag)
    context = {
        "blogs":blogs
    }
    return render(request,'blogs/blog_list.html',context)

def blog_category(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    context = {
        "blogs":blogs
    }
    return render(request,'blogs/blog_list.html',context)
    