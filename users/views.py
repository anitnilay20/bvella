
from django.shortcuts import render
import datetime
from users.forms import LoginForm,RegisterForm
from users.models import users
from products.models import orders
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest,HttpResponse


def register_done(request):
    name = "ola"
    phn = "00"
    if request.method == "POST":
        mlf = RegisterForm(request.POST)
        if mlf.is_valid():
            abc=mlf.save()
            email=mlf.cleaned_data['email']
            password = mlf.cleaned_data['password']
            try:
                email1 = users.objects.get(email=email, password=password)
                request.session['id'] = email1.id
            except ObjectDoesNotExist:
                pass
    else:
        name = "Error"
    form = RegisterForm(request.POST)
    return render(request, 'register_done.html', {"name": name, "phno": form})


def login(request):
    nexturl=request.GET['next']
    now=datetime.datetime.now()
    if request.method == 'POST':
        logform = LoginForm(request.POST)
        if logform.is_valid():
            email = logform.cleaned_data['email']
            password = logform.cleaned_data['password']
            try:
                email1 = users.objects.get(email=email, password=password)
                request.session['id'] = email1.id
                return render(request, 'login.html', {'date': now, 'user': email1, 'next':nexturl})
            except:
                n = "Invalid UserId Or Password"
                return HttpResponse("<h1>Invalid User Name or Password</h1>")
        else:
            n = "You left a field blank"
            return HttpResponse("<h1>You left a field empty</h1>")

def logout(request):
    try:
        del request.session['id']
        del request.session['cart']
    except KeyError:
      pass
    return render(request, 'loggedout.html')

def account(request):
    now = request.session["id"]
    try:
        cart = request.session['cart']
    except:
        cart = 0
    name= users.objects.get(id=now)
    add=name.address
    city=name.city
    pin=name.pincode
    email=name.email
    password=name.password
    phno=name.phno
    try:
        order = orders.objects.filter(user_id=now)
    except:
        order = "none"
    return render(request, 'account.html', {'name':name,'add':add,'city':city,'pin':pin,'email':email,
                                            'password':password,'phno':phno,'cart':cart,'order':order})

def update(request):
    id=request.session['id']
    mlf = RegisterForm(request.POST)
    if mlf.is_valid():
        name=mlf.cleaned_data['name']
        add =mlf.cleaned_data['address']
        city =mlf.cleaned_data['city']
        pin =mlf.cleaned_data['pincode']
        email =mlf.cleaned_data['email']
        password =mlf.cleaned_data['password']
        phno =mlf.cleaned_data['phno']
        users.objects.filter(id=id).update(name=name,address=add,city=city,pincode=pin,email=email,password=password,phno=phno)
        name = users.objects.get(id=id)
        add = name.address
        city = name.city
        pin = name.pincode
        email = name.email
        password = name.password
        phno = name.phno
        return render(request, 'account.html',
                      {'name': name, 'add': add, 'city': city, 'pin': pin, 'email': email, 'password': password,
                       'phno': phno})
    else:
        return HttpResponse("<h1>Invalid values in form reenter</h1><a href= url "+users.views.account+">Back</a>")