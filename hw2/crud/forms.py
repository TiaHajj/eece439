from django import forms
# from .models import Datbase, Item

class CreationForm(forms.Form):
    name= forms.CharField(label='Name', max_length=100)
    email= forms.CharField(label='Email', max_length=100)
    phone= forms.CharField(label='Phone', max_length=100)
    address= forms.CharField(label='Address', max_length=100)
    profession= forms.CharField(label='Profession', max_length=200)
    date= forms.DateTimeField(label='Date', required=False)

class ReadFromPhone(forms.Form):
    phone= forms.CharField(label='Phone', max_length=100)
    

class UpdateFormPhone(forms.Form):
    phone= forms.CharField(label='Phone', max_length=100, required=False)

class DeleteFromPhone(forms.Form):
    phone= forms.CharField(label='Phone', max_length=100, required=False)

