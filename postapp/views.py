from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    post_list = Post.objects.order_by('-register_date')
    context = { 'post_list': post_list }
    return render(request, 'postapp/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = { 
        'post': post,
    }
    return render(
        request, 'postapp/post_detail.html', context)

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.session['user_id']
            comment.register_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('postapp:detail', post_id=post.id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'postapp/comment_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.session['user_id']
            post.register_date = timezone.now()
            post.save()
            return redirect('postapp:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'postapp/post_form.html', context)

def comment_get(request):
    author = request.GET.get('username')
    c = Comment.objects.get(author=author)
    data=[]
    d = model_to_dict(c)
    data.append(d)
    return JsonResponse(data, safe=False)