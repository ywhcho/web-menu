from django.db import models
from django.urls import reverse


class Medicine(models.Model):
    """의약품 정보 모델"""
    EFFICACY_CHOICES = [
        ('antipyretic', '해열진통제'),
        ('digestive', '소화제'),
        ('cold', '감기약'),
        ('antibiotic', '항생제'),
        ('vitamin', '비타민'),
        ('dermatologic', '피부약'),
        ('other', '기타'),
    ]

    product_name = models.CharField('제품명', max_length=200)
    ingredient_name = models.CharField('성분명', max_length=200)
    efficacy = models.CharField('효능/효과', max_length=50, choices=EFFICACY_CHOICES)
    dosage = models.TextField('용법/용량')
    manufacturer = models.CharField('제조사', max_length=200)
    precautions = models.TextField('주의사항')
    created_at = models.DateTimeField('등록일', auto_now_add=True)

    class Meta:
        verbose_name = '의약품'
        verbose_name_plural = '의약품'
        ordering = ['-created_at']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('medicine:detail', kwargs={'pk': self.pk})

    def get_efficacy_display_korean(self):
        """효능 한글명 반환"""
        return dict(self.EFFICACY_CHOICES).get(self.efficacy, self.efficacy)

