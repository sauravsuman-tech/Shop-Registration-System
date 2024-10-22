from django import forms
from.models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']
    
    def clean_latitude(self):
        lat = self.cleaned_data['latitude']
        if lat <-90 or lat > 90:
            raise forms.ValidationError("Latitude must be between -90 and 90.")
        return lat
    
    def clean_longitude(self):
        lon = self.clean_latitude_data['longitude']
        if lon <-180 or lon > 180:
            raise forms.ValidationError("Longitude must be between -180 and 180.")
        return lon