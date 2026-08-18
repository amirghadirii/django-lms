from django import template
from blog.models import Post,Category,Comment
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog_popular_posts.html')
def popularposts():
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now()).order_by('published_date')[:4]
    return {"posts": posts}

@register.inclusion_tag('blog/blog_category.html')
def postcategory():
    posts = Post.objects.filter(status = 'published')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category = name).count()
    return {'categories':cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('core/latest_post.html')
def latest_post():
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now()).order_by('published_date')[:3]
    return {'posts':posts}