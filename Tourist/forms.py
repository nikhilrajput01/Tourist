from django import forms

class UserData(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder':'Email'
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'placeholder':'Phone Number'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder':'Password'
    }))

  