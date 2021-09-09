from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    date_of_joining = forms.DateField( 
        widget=forms.DateInput(attrs={
        'type': 'date'
    })
    )

    class Meta:
        model = Profile
        fields = "__all__"
