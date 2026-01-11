from django import forms
from .models import Medicine


class MedicineSearchForm(forms.Form):
    """의약품 검색 폼"""
    query = forms.CharField(
        label='성분명 검색',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '검색할 성분명을 입력하세요'
        })
    )


class MedicineForm(forms.ModelForm):
    """의약품 등록/수정 폼"""
    class Meta:
        model = Medicine
        fields = ('product_name', 'ingredient_name', 'efficacy', 'dosage', 
                  'manufacturer', 'precautions')
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'efficacy': forms.Select(attrs={'class': 'form-control'}),
            'dosage': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'precautions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
