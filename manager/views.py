from django.shortcuts import render

from . models import *



# Create your views here.

def index(request):
    return render(request,'manager/index.html')

def department(request):
    dep=Department.objects.all()
    return render(request,'manager/department.html',{'dep':dep})

def staff(request):
    staff=Employee.objects.all()
    return render(request,'manager/staffs.html',{'staff':staff})

def head(request):
    head=DepartmentHead.objects.all()
    return render(request,'manager/head.html',{'head':head})