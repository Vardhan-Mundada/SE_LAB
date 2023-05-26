from django.shortcuts import render
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

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


@login_required
def cat_questions(request, cat_id):
    category=models.Qcategory.objects.get(id=cat_id)
    questions=models.Question.objects.filter(category=category)
    return render(request, 'cat-questions.html', {'data':questions, 'category': category})