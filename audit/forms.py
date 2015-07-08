from django import forms
from django.forms import ModelForm
from .models import Count,Shelf
    
class ShelfForm(forms.ModelForm):
	class Meta:
		model = Shelf
		fields = ['shelf_no','row_1','row_2','row_3']

class ShelfCountForm(forms.Form):
    total_shelves = forms.IntegerField()