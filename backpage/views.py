from django.http import HttpResponse
from django.shortcuts import render
from .models import page

def index(request):
    return render(request,"index.html")
def products(request):
    return render(request,"products.html")
def account(request):
    return render(request, "account.html")
# def order(request):
#     return render(request,"order.html")
def home(request):
     if request.method=="POST":

        var1=request.POST["firstname"]
        var2=request.POST["lastname"]
        var3=request.POST["Address1"]
        var4=request.POST["Address2"]
        var5=request.POST["Email"]
        var6=request.POST["State"]
        var7=request.POST["Phn_no"]
        var8=request.POST["City"]
        var9=request.POST["Zip"]

        obj=page()
        obj.firstname=var1
        obj.lastname=var2
        obj.Address1=var3
        obj.Address2=var4
        obj.Email=var5
        obj.State=var6
        obj.Phn_no=var7
        obj.City=var8
        obj.Zip=var9
        obj.save()

        mydata=page.objects.all()
        return render(request,'home.html',{'page':mydata})
     return render (request,'home.html')

def func(request):
    if request.method=="GET":
        firstname=request.GET["firstname"]
        lastname=request.GET["lastname"]
        Address1=request.GET["Address1"]
        Address2=request.GET["Address2"]
        Email=request.GET["Email"]
        State=request.GET["State"]
        Phn_no=request.GET["Phn_no"]
        City=request.GET["City"]
        Zip=request.GET["Zip"]
       
        obj1=page()
        obj1.firstname=firstname
        obj1.lastname=lastname
        obj1.Address1=Address1
        obj1.Address2=Address2
        obj1.Email=Email
        obj1.State=State
        obj1.Phn_no=Phn_no
        obj1.City=City
        obj1.Zip=Zip
        obj1.save()

        myobject=page.objects.all()
        return render(request,'home.html',{'page':myobject})

    return render(request, 'func.html')





                        