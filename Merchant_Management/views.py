from django.shortcuts import render

from Merchant_Management.forms import MerchantForm
from Merchant_Management.models import CreateMerchant


def merchant_list(request):
    template = 'merchants/Marchant_List.html'
    all_merchant = CreateMerchant.objects.order_by('-id')
    context = {'list': all_merchant}
    return render(request, template, context)


def create_merchant(request):
    template = 'merchants/Create_Marchant.html'
    form = MerchantForm()
    if form.is_valid():
        form.save()
    return render(request, template, {'form': 'form'})
