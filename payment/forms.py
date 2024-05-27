from django import forms

from .models import Shipping


class ShippingForm(forms.ModelForm):
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1'}))
    address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), required=False)
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}), required=False)

    class Meta:
        model = Shipping
        fields = ('full_name', 'email', 'address1', 'address2', 'country', 'city', 'state', 'zipcode')
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'
