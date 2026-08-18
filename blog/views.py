from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment,User,Category
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_home(request,**kwargs):
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name = kwargs['tag_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,6)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)

def blog_single(request,pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submited')
    posts = get_object_or_404(Post,pk=pid)
    posts.counted_views +=1
    posts.save()
    new_count = posts.counted_views
    prev_post = Post.objects.filter(id__lt = posts.id,status = 'published',published_date__lte = timezone.now()).first()
    next_post = Post.objects.filter(id__gt = posts.id,status = 'published',published_date__lte = timezone.now()).last()
    
    comments = Comment.objects.filter(post = posts.id,approved = True)
    form = CommentForm()
    context = {
        'new_count':new_count,
        'posts':posts,
        'prev_post':prev_post,
        'next_post':next_post,
        'comments':comments,
        'form':form
        }
    return render(request,'blog/blog_single.html',context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now())
    posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)


def blog_search(request):
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)