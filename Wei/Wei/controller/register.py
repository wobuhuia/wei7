from django.shortcuts import render
from . import forms

def register(request):
	registerForm = forms.Forms
	return render(request, 'register/register.html', {'registerForm':registerForm})
