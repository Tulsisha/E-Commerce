from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app1.models import contactform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app1.models import CPersonM
from app1.models import CPersonM2
# Create your views here.
def Home(request):
  #return HttpResponse("helo tulsi")
 return render(request,"index.html")
def about(request):  
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
def register(request):
    return render(request,"register.html")
def contactform1(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        pincode=request.POST.get("pincode")
        message=request.POST.get("message")
        r=contactform(username=username,email=email,contact=contact,address=address,pincode=pincode,message=message)
        r.save()

        #return HttpResponse("Tulsi")
        return render(request,"contact.html",{"msg":"Tulsi"})

def registeruser(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        r=User.objects.create_user(first_name=name,email=email,username=username,password=password)
        r.save()
        #return HttpResponse("A/C Created")
         
        return render(request,"register.html",{"msg":"A/C Created"})

def loginform(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
    
        if user is not None:
            login(request,user)
            return redirect('/userhome')
        else:
            return redirect('/home')

def userhome(request):
    return render(request,'userhome.html')
def userlogout(request):
    logout(request)
    return redirect('/home')
def addrecord(request):
    return render(request,'addrecord.html')
def addcontact(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        city=request.POST.get("city")
        r=CPersonM(cperson=cperson,email=email,contact=contact,address=address,city=city)
        r.save()
        r1=CPersonM2(cperson=cperson,email=email,contact=contact,address=address,city=city)
        r1.save()

    #return HttpResponse("Tulsi")  
    return render(request,'addrecord.html',{'msg':'contact saved'})

def completerecord(request):
    r=CPersonM.objects.all
    return render(request,'completerecord.html',{'data':r})
def searchrecord(request):
    return render(request,'searchrecord.html')
def usersearchrecord(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        r=CPersonM.objects.get(cperson=cperson)
        return render(request,"usersearchrecord1.html",{'data':r})
def deleterecord(request):
    return render(request,"deleterecord.html")
def erase(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        r=CPersonM.objects.get(cperson=cperson)
        r.delete()
        return render(request,"deleterecord.html",{'msg':'successfully deleted'})
def update(request):
    return render(request,"update.html")
def userupdate(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        city=request.POST.get("city")
        CPersonM.objects.filter(cperson=cperson).update(email=email,contact=contact,address=address,city=city)
       
        return render(request,"update.html",{'msg':"successfully Updated"})

def changepassword(request):
    return render(request,"changepassword.html")
def userchangepassword(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        password=request.POST.get("password")
        r=User.objects.get(username=cperson)
        r.set_password(password)
        r.save()
        return render(request,"changepassword.html",{'msg':'change password'})
def removed(request):
    if request.method=="POST":
        rcperson=request.POST.get("rcperson")
        r=CPersonM.objects.filter(cperson=rcperson)
        r.delete()
        return redirect("/completerecord")
def undorecord(request):
    if request.method=="POST":
        cperson=request.POST.get("cperson")
        r=CPersonM2.objects.get(cperson=cperson)
        cperson=email=contact=address=city=''
        cperson=r.cperson
        email=r.email
        contact=r.contact
        address=r.address
        city=r.city
        r1=CPersonM(cperson=cperson,email=email,contact=contact,address=address,city=city)
        r1.save()
        return redirect('/completerecord')
def permanent(request):
    r1=CPersonM2.objects.all
    return render(request,'permanent.html',{'data':r1})




  