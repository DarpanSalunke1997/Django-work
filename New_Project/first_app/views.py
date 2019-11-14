from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord,Topic,WebPage,User_Info
from . import forms
from .forms import User_Modle_Form

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def Home(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(request,"index.html",date_dict)

def User(request):
    ui = User_Info.objects.order_by('name')
    ui_detail = {'user_info':ui}
    return render(request,"users.html",ui_detail)

def form_user(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Data Collected ... \n")
            print('Name :'+form.cleaned_data['name'])
            print('Email :'+form.cleaned_data['email'])
            print('Text :'+form.cleaned_data['text'])
    elif request.method == 'GET':
        print("AA TO GET PAN JOVE CHHE")
    return render(request,'form_data.html',{'form':form})

def Model_Form_User(request):
    form = User_Modle_Form()

    if request.method == 'POST':
        form=User_Modle_Form(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print("FORM IS INVALID")
    else:
        print("BIJU KAIK AAVE CHHE")
    
    return render(request,'model_base_form.html',{'form':form})
