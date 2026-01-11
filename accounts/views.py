from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, ProfileEditForm, CustomPasswordChangeForm


class CustomLoginView(LoginView):
    """로그인 뷰"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '사용자명을 입력하세요'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호를 입력하세요'})
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '로그인'
        return context


class CustomLogoutView(LogoutView):
    """로그아웃 뷰"""
    next_page = '/'


def signup(request):
    """회원가입 뷰"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요.')
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form, 'title': '회원가입'})


@login_required
def profile_edit(request):
    """회원정보 수정 뷰"""
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('accounts:profile_edit')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'accounts/profile_edit.html', {'form': form, 'title': '회원정보 수정'})


@login_required
def password_change(request):
    """비밀번호 변경 뷰"""
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션 유지
            messages.success(request, '비밀번호가 변경되었습니다.')
            return redirect('accounts:profile_edit')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'accounts/password_change.html', {'form': form, 'title': '비밀번호 변경'})

