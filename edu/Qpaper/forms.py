from .models import *

from django.forms import forms

class bookingform(forms.Form):
    bookingtype=forms

class tourbookingform(forms.Form):
    class Meta:
        models=tourbooking
        fields=('name', 'phone', 'email', 'checkindate', 'checkoutdate', 'numberofadult', 'numberofchildren')
   