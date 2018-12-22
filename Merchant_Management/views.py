from django.shortcuts import render

from Merchant_Management.forms import MerchantForm


def merchant_list(request):
    template = 'merchants/Marchant_List.html'
    return render(request, template)


def create_merchant(request):
    template = 'merchants/Create_Marchant.html'
    form = MerchantForm()
    if form.is_valid():
        form.save()
    return render(request, template, {'form': 'form'})
