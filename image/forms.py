from django import forms
from .models import Image
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

    def clean_renewal_date(self):
        data = self.cleaned_data['title']

        # Check if a date is not in the past.
        if data.endswith('jpg'):
            raise ValidationError(_('Invalid date - renewal in past'))
        if data!=1:
        # Check if a date is in the allowed range (+4 weeks from today).

            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data