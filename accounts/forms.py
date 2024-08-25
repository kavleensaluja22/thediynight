from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    product_uid = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Review
        fields = ['rating', 'text', 'media', 'product_uid']