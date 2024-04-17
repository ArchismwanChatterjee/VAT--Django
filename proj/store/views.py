from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import *
import os
# Create your views here.
def test(request):
    return HttpResponse('testing the page')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def add(request):
    a=request.GET['a1']
    b=request.GET['a2']
    x=request.GET['btn']
    if x=="add":
        c=int(a)+int(b)
        return render(request,'about.html',{'c':c})
    elif x=="sub":
        c=int(a)-int(b)
        return render(request,'about.html',{'c':c})
    elif x=="mul":
        c=int(a)*int(b)
        return render(request,'about.html',{'c':c})
    elif x=="div":
        c=int(a)//int(b)
        return render(request,'about.html',{'c':c})
    else:
        return HttpResponse('no')
def insert(request):
    return render(request,'insert.html')
def ins(request):
    u=user() # function name and table name cannot be same
    u.name=request.GET['a1']
    u.email=request.GET['a2']
    u.pwd=request.GET['a3']
    u.save()
    return render(request,'insert.html')

def insert_2(request):
    return render(request,'student.html')

def ins2(request):
    s = Student() 
    s.name = request.GET['a1']
    s.email = request.GET['a2']
    s.phno = request.GET['a3']
    s.addr = request.GET['a4']
    s.fname = request.GET['a5']
    s.mname = request.GET['a6']
    s.city = request.GET['a7']
    s.state = request.GET['a8']
    s.save()
    return render(request,'student.html')

def show(request):
    u=user.objects.all()
    return render(request,'show.html',{'x':u}) # json format 
def show2(request):
    u=Student.objects.all()
    return render(request,'show2.html',{'x':u})
def dele(request,id):
    u=user.objects.get(id=id)
    u.delete()
    return redirect("../show")
def edit(request,id):
    u=user.objects.get(id=id)
    return render(request,'edit.html',{'u':u})
def upd(request,id):
    u=user.objects.get(id=id)
    u.name=request.GET['a1']
    u.email=request.GET['a2']
    u.pwd=request.GET['a3']
    u.save()
    return redirect("../show")
def upload(request):
    return render(request,'upload.html')
def upld(request):
    if request.method=='POST':
        #a=str(request.FILES['a1'])
        #if a[-4:]=="jfif":
         #   return HttpResponse("no file")
        handle_uploaded_file(request.FILES['a1'],str(request.FILES['a1']))
        url="upload/"+str(request.FILES['a1'])
        u=picfile()
        u.pname=str(request.FILES['a1'])
        u.purl=url
        u.save()
        return render(request,'upload.html')
    return render(request,'upload.html')
def handle_uploaded_file(file, filename):
    if not os.path.exists('store/static/upload/'):
        os.mkdir('store/static/upload/')

    with open('store/static/upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
def fpic(request):
    u=picfile.objects.all()
    return render(request,'picshow.html',{'u':u})