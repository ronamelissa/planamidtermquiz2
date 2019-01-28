from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm

from datetime import datetime
# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts']=posts
    return render(request, "index.html", context)

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'create.html', context)
    else:
        context['form'] = PostForm(initial={'date_created': datetime.now().date()})
        return render(request, 'create.html', context)

def update(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated')
    else:
        post = Post.objects.get(id=post_id)
        context = {}
        context['form'] = PostForm(instance=post)
        return render(request, 'update.html', context)

def comment(request, post_id):
    ppost = get_object_or_404(Post, post_id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_text = post_text
            comment.save()
            return HttpResponse("Post updated")
    else:
        context = {}
        context['form'] = PostForm(instance=post)
        return render(request, 'comment.html', context)
