"""from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from accounts.forms import UserRegisterForm
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username_input = request.POST.get('username')
        password = request.POST.get('password')

        if not username_input or not password:
            messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')
            return redirect('account:login')

        user_obj = User.objects.filter(Q(email=username_input) | Q(username=username_input)).first()
        if user_obj:
            user = authenticate(request,username=user_obj.username,password=password)
            if user:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید.')
                return redirect('/')

        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        return redirect('account:login')

    return render(request, 'account/login.html')
    


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید.')
    return redirect('/')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'ثبت‌ نام با موفقیت انجام شد.')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'account/signup.html', {'form': form})"""