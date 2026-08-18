from django import template
from course.models import Course,Category
from django.utils import timezone


register = template.Library()

@register.inclusion_tag('course/course_related.html')
def courserelated(course_id):
    current_course = Course.objects.get(id=course_id)
    related = Course.objects.filter(
        category=current_course.category, 
        status='published'
    ).exclude(id=course_id)[:3]
    
    return {"courses": related}

@register.inclusion_tag('course/course_category.html')
def coursecategory():
    courses = Course.objects.filter(status = 'published')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = courses.filter(category = name).count()
    return {'categories':cat_dict}


@register.inclusion_tag('core/latest_course.html')
def latest_course():
    courses = Course.objects.filter(status = 'published',published_date__lte = timezone.now()).order_by('published_date')[:3]
    return {'courses':courses}