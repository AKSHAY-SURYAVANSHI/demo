
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models  import signup_student
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.forms import inlineformset_factory


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup_organization(request):
    if request.method== 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            Name_of_the_organisation=form.cleaned_data.get('Name_of_the_organization')
           
            return redirect("home")
    else:
        form=UserCreationForm()
    return render(request,"authentication/signup_organization.html",{'form':form})

def signup_freelance_teacher(request):
    return render(request,"authentication/signup_freelance_teacher.html")


def signup_student(request):
    form = UserCreationForm()

    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 

    context = {'form':form}
    return render(request,"authentication/signup_student.html")


def Org_login_page(request):
    return render(request,"authentication/Org_login_page.html")

def Flt_login_page(request):
    return render(request,"authentication/Flt_login_page.html")
  
def Student_login_page(request):
    return render(request,"authentication/Student_login_page.html")

def Prg_login_page(request):
    return render(request,"authentication/Prg_login_page.html")

def Dept_login_page(request):
    return render(request,"authentication/Dept_login_page.html")

def vision(request):
    return render(request,"authentication/vision.html")   


