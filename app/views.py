from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.
@csrf_exempt
def indexpage(request):
   if request.user.is_authenticated:
      ses=Question.objects.filter(user=request.user)
      hi=request.GET.get("qry")
      if hi is None:
          hi=""
      profile=Userdetail.objects.get(user=request.user)
      
   
   


      if request.method=="POST" :
         a=request.POST['ques']
        
        
     

      
         obj=Question(ques=a,user=profile)
         obj.save()
         

      
      return render(request,'index.html',{"ses":ses,"hi":hi})
   return render(request,'index.html')


def login(request):
   if request.method=="POST":
        usern=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=usern,password=passw)
        if user is not None:
            print("yes")
            auth.login(request,user)
            if request.user.is_authenticated:
                print("yes ")
                return HttpResponseRedirect('/')
   return render(request,"pages-login.html")

def register(request):
    if request.method=="POST":
        fname=request.POST['fn']

       
        email=request.POST['email']
        usern=request.POST['username']
        passw=request.POST['pass']
        print(usern,passw)
        if User.objects.filter(username=usern).exists():
          print("hai")

        else:
            user=Userdetail.objects.create_user(username=usern,first_name=fname,email=email,password=passw)    
            user.save()
            user=auth.authenticate(username=usern,password=passw)
            if user is not None:
                print("yes")
                auth.login(request,user)
                if request.user.is_authenticated:
                    print("yes ")
                    return HttpResponseRedirect('/')
    return render(request,"pages-register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

@csrf_exempt
def doc(request):
    if request.user.is_authenticated:
      ses=Question.objects.filter(user=request.user)
      hi=request.GET.get("qry")
      if hi is None:
          hi=""
      profile=Userdetail.objects.get(user=request.user)
      
   
   


      if request.method=="POST" :
          b=request.FILES['file']
          obj=Docfile(user=profile,doc=b)
          obj.save()
        
        
     

      
      

      
      return render(request,'index.html',{"ses":ses,"hi":hi})
    return render(request,'index.html')
@csrf_exempt
def excel(request):
    if request.user.is_authenticated:
      ses=Question.objects.filter(user=request.user)
      hi=request.GET.get("qry")
      if hi is None:
          hi=""
      profile=Userdetail.objects.get(user=request.user)
      
   
   


      if request.method=="POST" :
          b=request.FILES['file']
          obj=Docfile(user=profile,excel=b)
          obj.save()
        
        
     

      
      

      
      return render(request,'index.html',{"ses":ses,"hi":hi})
    return render(request,'index.html')
@csrf_exempt
def pdf(request):
    if request.user.is_authenticated:
      ses=Question.objects.filter(user=request.user)
      hi=request.GET.get("qry")
      if hi is None:
          hi=""
      profile=Userdetail.objects.get(user=request.user)
      
   
   


      if request.method=="POST" :
          b=request.FILES['file']
          obj=Pdffile(user=profile,pdf=b)
          obj.save()
        
        
     

      
      

      
      return render(request,'index.html',{"ses":ses,"hi":hi})
    return render(request,'index.html')