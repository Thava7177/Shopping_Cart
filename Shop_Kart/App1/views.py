from django.shortcuts import render,redirect
 
from django.http import JsonResponse

from App1.form import *

from . models import * 

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

import json

def home(request):
    trand=Product.objects.filter(tranding=1)
    return render(request,"shop/index.html",{"products":trand})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged In Successfully")
    return redirect('/')

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"Fav":fav})
    else:
        return redirect("/")

def remove_fav(request,fid):
    favitem=Favourite.objects.get(id=cid)
    favitem.delete()
    return redirect("/favviewpage")

def order(request):
    form1=Orders()
    if request.method=='POST':
        form1=Orders(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request,"Order Successfully Placed !")
            return render('shop/success.html')
    return render(request,"shop/order.html",{'form2':form1})


def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favourite '},status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added To Favourtite'},status=200)
        else:
            return JsonResponse({'status':'Login To Add Favourtite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"Cart":cart})
    else:
        return redirect("/")

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart '},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added To Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Stock Not Available '},status=200) 
        else:
            return JsonResponse({'status':'Login To Add Cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged In Successfully")
                return redirect('/')
            else:
                messages.error(request,"Invalid User Name Or Password")
                return redirect("/login")
        return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registation Success You Can Login Now ...!")
            return redirect('login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})

def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products,"catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
              messages.warning(request,"No Such Product Found")
              return redirect('collections')
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')


