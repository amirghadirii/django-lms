from django.shortcuts import render,get_object_or_404
from course.models import Course,Comment,Instructor,Category
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from course.forms import CommentForm
from django.contrib import messages

# Create your views here.
def course_home(request, **kwargs):
    courses = Course.objects.filter(status='published', start_date__lte=timezone.now())
    if kwargs.get('cat_name'):
        courses = courses.filter(category__name=kwargs['cat_name'])   
    if kwargs.get('author_username'):
        courses = courses.filter(instructor__name=kwargs['author_username'])
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    try:
        courses = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        courses = paginator.get_page(1)
        
    context = {'courses': courses}
    return render(request, 'course/course.html', context)



def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug, status='published')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.course = course 
            if request.user.is_authenticated:
                new_comment.user = request.user 
            new_comment.save()
            messages.success(request, 'دیدگاه شما با موفقیت ثبت شد و پس از تایید نمایش داده می‌شود.')
        else:
            messages.error(request, 'ثبت دیدگاه با خطا مواجه شد. لطفاً فرم را بررسی کنید.')
    comments = Comment.objects.filter(course=course, approved=True)
    form = CommentForm()
    
    context = {
        'course': course,
        'comments': comments,
        'form': form
    }
    return render(request, 'course/course-details.html', context)


def course_category(request,cat_name):
    courses = Course.objects.filter(status = 'published',published_date__lte = timezone.now())
    courses = courses.filter(category__name = cat_name)
    context = {'courses':courses}
    return render(request,'course/course.html',context)