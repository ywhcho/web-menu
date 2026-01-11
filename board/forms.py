from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """게시글 작성/수정 폼"""
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '제목을 입력하세요'
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 10,
            'placeholder': '내용을 입력하세요'
        })
    )

    class Meta:
        model = Post
        fields = ('title', 'content')
