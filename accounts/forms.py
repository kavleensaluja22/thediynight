from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text', 'media']

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'payment_method']

from django import forms
from .models import SellerProfile

class KYCForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['phone', 'address', 'aadhar_number', 'pan_number']

