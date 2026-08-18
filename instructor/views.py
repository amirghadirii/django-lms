from django.shortcuts import render,get_object_or_404
from instructor.models import Instructor
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from course.models import Course

def instructor_home(request):
    instructor_list = Instructor.objects.all().order_by('name')
    paginator = Paginator(instructor_list, 6)
    page_number = request.GET.get('page')

    try:
        teachers = paginator.get_page(page_number)
    except PageNotAnInteger:
        teachers = paginator.get_page(1)
    except EmptyPage:
        teachers = paginator.get_page(paginator.num_pages)

    context = {'teachers': teachers}
    return render(request, 'instructor/instructor.html', context)


def instructor_single(request, slug):
    teacher = get_object_or_404(Instructor, slug=slug)
    courses = Course.objects.filter(instructor=teacher, status='published')
    
    context = {'teacher': teacher,'courses': courses,}
    return render(request, 'instructor/ins_details.html', context)
