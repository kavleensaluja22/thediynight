from .models import ProFile


from django import forms
from .models import Address

# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['street', 'city', 'state', 'zip_code']
#         widgets = {
#             'street': forms.TextInput(attrs={'class': 'form-input'}),
#             'city': forms.TextInput(attrs={'class': 'form-input'}),
#             'state': forms.TextInput(attrs={'class': 'form-input'}),
#             'zip_code': forms.TextInput(attrs={'class': 'form-input'}),
#         }

from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['number', 'type']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-input'}),
            'type': forms.Select(choices=[('mobile', 'Mobile'), ('home', 'Home'), ('work', 'Work')], attrs={'class': 'form-input'}),
        }

from django import forms
from .models import ProFile

from django import forms
from .models import ProFile

class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'user-name'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'id': 'user-email'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'id': 'user-password'}),
        required=False
    )
    profile_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-input'}),
        required=False
    )
    email_verified = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-input'}),
        required=False
    )

    class Meta:
        model = ProFile
        fields = ['profile_image', 'email_verified']  # Fields to be included in the form

    def __init__(self, *args, **kwargs):
        # Include instance if needed for pre-populating form fields
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'user'):
            self.fields['name'].initial = self.instance.user.first_name
            self.fields['email'].initial = self.instance.user.email


from django import forms
# from .models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'email', 'phone', 'address']
from django import forms
from .models import ProFile

class ProFileForm(forms.ModelForm):
    class Meta:
        model = ProFile
        fields = ['name', 'email', 'phone', 'address', 'profile_image']


from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'street', 'city', 'state', 'country', 'zip_code', 'is_default']

