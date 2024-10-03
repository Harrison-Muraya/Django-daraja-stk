from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import lipa_na_mpesa_online

def lipa_na_mpesa(request):
    phone_number = request.GET.get('phone_number')
    amount = request.GET.get('amount')
    account_reference = request.GET.get('account_reference', 'Ref123')
    transaction_desc = request.GET.get('transaction_desc', 'Payment description')

    response = lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc)
    return JsonResponse(response)
