from django import forms
from .models import *

class Profilereg(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name', 'email', 'phone','address']    
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }

class Clgreg(forms.ModelForm):
    class Meta:
        model = clgdet
        fields = ['college', 'school', 'branch','degree']    
        widgets = {
            'college': forms.TextInput(attrs={'class':'form-control'}),
            'school': forms.TextInput(attrs={'class':'form-control'}),
            'branch': forms.TextInput(attrs={'class':'form-control'}),
            'degree': forms.TextInput(attrs={'class':'form-control'}),
        }


