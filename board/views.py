from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F
from .models import Post
from .forms import PostForm


def post_list(request):
    """게시글 목록 뷰"""
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)  # 한 페이지에 10개씩
    
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'board/board_list.html', {
        'posts': posts,
        'title': '게시판'
    })


def post_detail(request, pk):
    """게시글 상세 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가
    Post.objects.filter(pk=pk).update(views=F('views') + 1)
    post.refresh_from_db()
    
    return render(request, 'board/board_detail.html', {
        'post': post,
        'title': post.title
    })


@login_required
def post_create(request):
    """게시글 작성 뷰"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '게시글이 작성되었습니다.')
            return redirect('board:detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'board/board_form.html', {
        'form': form,
        'title': '게시글 작성'
    })


@login_required
def post_edit(request, pk):
    """게시글 수정 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 수정 가능
    if post.author != request.user:
        messages.error(request, '게시글 수정 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '게시글이 수정되었습니다.')
            return redirect('board:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'board/board_form.html', {
        'form': form,
        'post': post,
        'title': '게시글 수정'
    })


@login_required
def post_delete(request, pk):
    """게시글 삭제 뷰"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 삭제 가능
    if post.author != request.user:
        messages.error(request, '게시글 삭제 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('board:list')
    
    return render(request, 'board/board_delete.html', {
        'post': post,
        'title': '게시글 삭제'
    })

