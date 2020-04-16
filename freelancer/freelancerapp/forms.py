from django import forms 
from .models import Login,Projects

class signupForm(forms.ModelForm): 
	class Meta: 
		model = Login 
		fields="__all__"
		widgets = {
        'password': forms.PasswordInput(),
		}

class loginForm(forms.ModelForm): 
	class Meta: 
		model = Login 
		fields=("name","password")
		widgets = {
        'password': forms.PasswordInput(),
		}

class post_project_form(forms.ModelForm):
	class Meta:
		model = Projects
		fields =("project_id","name","desc","status","skills","mem_needed","min_payment","max_payment","days")
		widgets={
			'project_id':forms.NumberInput(attrs={'class': "input-lg"}),
			'name':forms.TextInput(attrs={'class': "input-lg"}),
			'desc':forms.Textarea(attrs={'class': "input-lg"}),
			'status':forms.TextInput(attrs={'class': "input-lg"}),
			'skills':forms.TextInput(attrs={'class': "input-lg"}),
			'mem_needed':forms.TextInput(attrs={'class': "input-lg"}),
			'min_payment':forms.NumberInput(attrs={'class': "input-lg"}),
			'max_payment':forms.NumberInput(attrs={'class': "input-lg"}),
			'days':forms.NumberInput(attrs={'class': "input-lg"}),

		}
		
		