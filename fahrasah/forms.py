from django import forms 
from .models import Project, Page, Field  


class EditProjectForm(forms.ModelForm): 


    class Meta: 
        model = Project 
        fields = '__all__' 
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'title': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'website_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 


            'website_field': forms.Select(attrs={'class': 'form-control'}), 
            'website_activity': forms.Select(attrs={'class': 'form-control'}), 

        }

    

class EditPageForm(forms.ModelForm):

    class Meta:
        model = Page 
        fields = '__all__' 
        exclude = ['project']

        widgets = {
     'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'reference': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'url': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 

 

        }

class EditFieldForm(forms.ModelForm):

    class Meta:
        model = Field 
        fields = '__all__' 
        exclude = ['project', 'page']

        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'description': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'reference': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'url': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'database': forms.Select(attrs={'class': 'form-control'}), 
            'cmd': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 

        }
        