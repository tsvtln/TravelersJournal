from django import forms
from django.core.exceptions import ValidationError

from travelers.models import Traveler, Trip


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Enter a unique nickname...',
                'aria-describedby': 'id_nickname_helptext',
                'maxlength': 30,
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter a valid email address...',
                'maxlength': 30,
                'required': True,
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter a country code like <BGR>...',
                'maxlength': 3,
                'required': True,
            }),
        }
        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'country': 'Country:',
        }
        help_texts = {
            'nickname': '*Nicknames can contain only letters and digits.',
        }


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ['traveler']
        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': 'Enter a short destination note...',
                'required': True,
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Share your exciting moments...',
                'rows': 5,
                'cols': 40,
                'required': True,
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'required': True,
            }),
            'duration': forms.NumberInput(attrs={
                'min': 1,
                'value': 1,
                'required': True,
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'An optional image URL...',
            }),
        }
        labels = {
            'destination': 'Destination:',
            'summary': 'Summary:',
            'start_date': 'Started on:',
            'duration': 'Duration:',
            'image_url': 'Image URL:',
        }
        help_texts = {
            'duration': '*Duration in days is expected.',
        }

    def clean_destination(self):
        destination = self.cleaned_data.get('destination')
        if len(destination) < 3 or len(destination) > 100:
            raise ValidationError("Destination must be between 3 and 100 characters.")
        return destination


