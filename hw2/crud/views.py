from django.shortcuts import render
from .models import Datbase, Item
from .forms import CreationForm, ReadFromPhone, UpdateFormPhone, DeleteFromPhone
#defining the functions 
def index (request):
    return render(request, 'crud/index.html')

from datetime import date
def create(request):
    if request.method == 'POST':
        # handle when user posts data
        form=CreationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            address=form.cleaned_data['address']
            profession=form.cleaned_data['profession']
            date=form.cleaned_data['date']
            # save data to database
            data=Datbase(name=name, email=email, phone=phone, address=address, profession=profession, date=date)
            data.save()
            return render(request, 'crud/create.html', {'form':form, 'message':f'{name} has been added to the database'})

    form=CreationForm()
    return render(request, 'crud/create.html', {'form': form})

def read(request):
    if request.method == 'POST':
        # handle when user posts data
        form=ReadFromPhone(request.POST)
        if form.is_valid():
            phone=form.cleaned_data['phone']
            # save data to database
            data=Datbase.objects.filter(phone=phone)
            if data.count() == 0:
                return render(request, 'crud/read.html', {'form':form, 'message':'No data found'})
            data=data[0]
            return render(request, 'crud/read.html', {'form':form, 'name':data.name, 'email':data.email, 'phone':data.phone, 'address':data.address, 'profession':data.profession, 'date':data.date})
    form=ReadFromPhone()
    return render(request, 'crud/read.html', {'form': form})
    

def update(request):
    updateform1 = UpdateFormPhone()
    if request.method == 'POST':
        if request.POST.get('name'):
            #user is updating the data
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            profession=request.POST.get('profession')
            date
            data=Datbase.objects.get(phone=phone)
            data.name=name
            data.email=email
            data.phone=phone
            data.address=address
            data.profession=profession
            data.date=date.today()
            data.save()
            return render(request, 'crud/update.html', {'updateform1':updateform1, 'showForm2':False, 'message':f'{name} has been updated'})
        else:
            form = UpdateFormPhone(request.POST)
            if form.is_valid():
                phone=form.cleaned_data['phone']
                if phone == '':
                    return render(request, 'crud/update.html', {'updateform1':updateform1, 'showForm2':False})
                data=Datbase.objects.filter(phone=phone)
                if data.count() == 0:
                    return render(request, 'crud/update.html', {'updateform1':updateform1, 'showForm2':False, 'message':'No data found'})
                data=data[0]
                return render(request, 'crud/update.html', {'updateform1':updateform1, 'showForm2':True, 'name':data.name, 'email':data.email, 'phone':data.phone, 'address':data.address, 'profession':data.profession})
    return render(request, 'crud/update.html', {'updateform1':updateform1, 'showForm2':False})

def delete(request):    
    if request.method == 'POST':
        # handle when user posts data
        form= DeleteFromPhone(request.POST)
        if form.is_valid():
            phone=form.cleaned_data['phone']
            # delete
            data=Datbase.objects.filter(phone=phone)
            if data.count() == 0:
                return render(request, 'crud/delete.html', {'form':form, 'message':'No data found'})
            data=data[0]
            data.delete()
            return render(request, 'crud/delete.html', {'form':form, 'message':f'{phone} has been deleted'})
    form=DeleteFromPhone()
    return render(request, 'crud/delete.html', {'form': form,})

# Create your views here.
