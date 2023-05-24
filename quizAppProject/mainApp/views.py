from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    msg=None
    form=forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='Registered'
    return render(request, 'registration/register.html', {'form':form, 'msg':msg})


def all_categories(request):
    catData=models.Qcategory.objects.all()
    return render(request, 'all-category.html', {'data': catData})