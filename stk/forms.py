from django import forms

class MpesaForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=12)
