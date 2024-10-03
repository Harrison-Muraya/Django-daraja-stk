import requests
from django.shortcuts import render
from .forms import MpesaForm
from django.conf import settings

def get_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    response = requests.get(api_url, auth=(consumer_key, consumer_secret))
    token = response.json().get("access_token")
    
    return token

def format_phone_number(phone_number):
    """Convert phone number to 254 format."""
    if phone_number.startswith('0'):
        # Replace leading 0 with 254 (Kenya's country code)
        return '254' + phone_number[1:]
    elif phone_number.startswith('+'):
        # Remove the + sign if present
        return phone_number[1:]
    return phone_number

def lipa_na_mpesa_online(phone_number, amount):
    phone_number = format_phone_number(phone_number)  # Ensure correct phone format
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": settings.MPESA_PASSWORD,
        "Timestamp": "20241003010101",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,  # Use formatted phone number
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,  # Use formatted phone number
        "CallBackURL": "https://yourdomain.com/payments/callback/",
        "AccountReference": "MpesaPayment",
        "TransactionDesc": "Payment for goods"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def initiate_payment(request):
    if request.method == "POST":
        form = MpesaForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            amount = 50  # You can change this to a dynamic amount

            # Call the function to initiate payment
            response = lipa_na_mpesa_online(phone_number, amount)
            return render(request, 'base/confirmation.html', {'response': response})
    else:
        form = MpesaForm()

    return render(request, 'base/pay.html', {'form': form})
