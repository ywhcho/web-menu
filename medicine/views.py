from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Medicine
from .forms import MedicineSearchForm


def medicine_list(request):
    """의약품 목록 메인 페이지"""
    medicines = Medicine.objects.all()[:6]  # 최근 6개만 표시
    return render(request, 'medicine/medicine_list.html', {
        'medicines': medicines,
        'title': '의약정보'
    })


def medicine_search(request):
    """성분명 검색 뷰"""
    query = request.GET.get('query', '')
    medicines = []
    
    if query:
        medicines = Medicine.objects.filter(
            Q(ingredient_name__icontains=query) | 
            Q(product_name__icontains=query)
        )
    
    paginator = Paginator(medicines, 10)
    page_number = request.GET.get('page')
    medicines_page = paginator.get_page(page_number)
    
    form = MedicineSearchForm(initial={'query': query})
    
    return render(request, 'medicine/medicine_search.html', {
        'form': form,
        'medicines': medicines_page,
        'query': query,
        'title': '의약품 검색'
    })


def medicine_efficacy(request):
    """효능별 보기 뷰"""
    efficacy = request.GET.get('efficacy', '')
    medicines = []
    
    if efficacy:
        medicines = Medicine.objects.filter(efficacy=efficacy)
    
    paginator = Paginator(medicines, 10)
    page_number = request.GET.get('page')
    medicines_page = paginator.get_page(page_number)
    
    # 효능 목록
    efficacy_choices = Medicine.EFFICACY_CHOICES
    
    return render(request, 'medicine/medicine_efficacy.html', {
        'medicines': medicines_page,
        'efficacy_choices': efficacy_choices,
        'selected_efficacy': efficacy,
        'title': '효능별 의약품'
    })


def medicine_detail(request, pk):
    """의약품 상세 정보 뷰"""
    medicine = get_object_or_404(Medicine, pk=pk)
    
    return render(request, 'medicine/medicine_detail.html', {
        'medicine': medicine,
        'title': medicine.product_name
    })

