from django.shortcuts import render,redirect
from core.forms import NewsletterForm,CaptchaTestForm
from django.contrib import messages
from course.models import Course,Category
from instructor.models import Instructor
from blog.models import Post
from django.utils import timezone
# Create your views here.
def index_view(request):
    courses = Course.objects.all()[:6]
    categories = Category.objects.all()
    teachers = Instructor.objects.all()[:4]
    posts = Post.objects.all()[:3]
    
    
    context={'courses':courses,'categories':categories,'teachers':teachers,'posts':posts}
    return render(request,'core/index.html',context)


def about_view(request):
    return render(request,'core/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = 'unknown'
            contact.save()
            messages.add_message(request,messages.SUCCESS,'پیام شما با موفقیت ارسال شد')
        else:
            messages.add_message(request,messages.ERROR,'لطفاً فرم را صحیح پر کنید')
    form = CaptchaTestForm()
    return render(request,'core/contact.html',{'form':form})



def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        next_url = request.POST.get("next") or "/"
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'ایمیل با موفقیت ثبت شد')
            return redirect(next_url)
        else:
            messages.add_message(request,messages.ERROR,'این ایمیل قبلاً ثبت شده یا معتبر نیست')
            return redirect(next_url)


def faq_view(request):
    return render(request,'core/faq.html')

def search_view(request):
    posts = Post.objects.filter(status = 'published',published_date__lte = timezone.now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    
    context = {'posts':posts}
    return render(request,'core/index.html',context)


def maintenance(request):
    return render(request, 'maintenance.html')


def page_not_found(request, exception):
 return render(request, '404.html', status=404)