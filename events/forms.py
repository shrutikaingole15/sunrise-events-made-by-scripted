from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'event_date', 
                 'venue_location', 'additional_notes']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'additional_notes': forms.Textarea(attrs={'rows': 4}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)