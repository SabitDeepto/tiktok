from django import forms

from Merchant_Management.models import CreateMerchant


class MerchantForm(forms.ModelForm):
    class Meta:
        model = CreateMerchant
        fields = ['firstName', 'email', 'phone']
#         widgets = {
#             'ambassador_name': forms.TextInput(
#                 attrs={'class': "form-control", 'placeholder': "Enter Ambassador name", 'type': "text"}),
#             'email': forms.TextInput(
#                 attrs={'class': "form-control", 'placeholder': "Your Email", 'type': "text"}),
#             'phone': forms.TextInput(
#                 attrs={'class': "form-control", 'placeholder': "Your phone number", 'type': "text"}),
# }
