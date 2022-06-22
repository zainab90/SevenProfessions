from django import forms
from serviceApp.models import Service, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'cat_name',
            'cat_image',
            'cat_details'
        ]


class ServiceForm (forms.ModelForm):
    serv_details=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder':'Enter'}),label='Enter Service Details')
    class Meta:
        model=Service
        fields=[
            'serv_name',
            'serv_details',
            'serv_Img',
        ]