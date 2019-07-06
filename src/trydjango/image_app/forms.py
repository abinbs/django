from django import forms
from .models import *

class HotelForm(forms.ModelForm):
    class Meta:
        model=HotelFormfoields=['name','hotel_Main_Img']
