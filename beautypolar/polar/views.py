from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.

def home(request):
     if not request.user.is_staff:
        return render(request , "home.html")          # Logout Function
     return redirect("admin_home")



def contact(request):

    return render(request, "contact.html")

def about(request):

    return render(request, "about.html")


def loginUser(request):
    error = ""
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]
        print(email, password)
        user = authenticate(username = email, password=password)
        # regis = registration.objects.get(user = user_ko)
        # regis = get_object_or_404(registration, user=user)
        # print(user)
        try:
            regis = registration.objects.get(user = user)     #User Login
            print(regis)
        except registration.DoesNotExist:
            print("None")
        if user:
            if regis.status.status == "Accept":
                login(request, user)
                error = "yes"

            else:
                error = "notaccept"
        else:
            error = "not"

    message={
        "error_message" : error
    }

    return render(request, "login.html", message)

def register(request):
    error = ""
    if request.method == "POST":
        name = request.POST["fname"]
        last = request.POST["lname"]
        contact = request.POST["contact"]
        gender = request.POST["gender"]           # Registration
        email = request.POST["email"]
        password = request.POST["pass"]
        image = request.POST["image"]
        sta = User_status.objects.get(status="Pending")
        print(sta)
        user_data = User.objects.create_user(username=email,  password=password, first_name=name , last_name=last)
        sign = registration.objects.create(status = sta, user = user_data,contact = contact,gender = gender,email = email,image = image, name=name,last=last, password = password)
        error = "yes"
    message={
        "error_message" : error
    }
    return render(request, "register.html", message)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    sign = Apponitment.objects.all()
    new = 0
    total = 0
    confrim = 0                                # Admin Home Page Show EveryThink
    for x in sign:
        if x.status.status == "Pending":
            new +=1
        elif x.status.status == "Accept":
            confrim +=1
        total+=1
    d = {'new':new, 'confrim': confrim, 'total': total}
    return render(request, "admin_home.html", d)


def logoutUser(request):
    if not request.user.is_staff:
        return redirect("loginUser")          # Logout Function
    logout(request)
    return redirect("loginUser")


def admin_login(request):
    error = ""
    if request.method == "POST":
        user = authenticate(username = request.POST["email"], password = request.POST["pass"])
        try:
            if user.is_staff:
                login(request, user)                          # admin Login
                error = "yes"
                return redirect("/admin_home")
            else:
                error = "not"
        except:
            error = "not"
    message = {"error_message" : error}
    return render(request, "admin.html", message)


def View_user(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    pro = registration.objects.all()
    print(pro)                 # Admin site Function view All user
    messge = {'user' : pro}
    return render(request, 'all_user.html', messge)


def remove_allUser(request, pid):
  user = registration.objects.get(id=pid)
  user.delete()
  return redirect("View_user")


def View_new_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    status = User_status.objects.get(status="Pending")
    pro = registration.objects.filter(status=status)
    d = {'user' : pro}
    return render(request, 'request_user.html', d)


def Assign_user_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = False
    book = registration.objects.get(id=pid)
    if request.method == "POST":
        n = request.POST['book']
        s = request.POST['status']
        print(s)
        username = User.objects.get(username=n)
        book.user = username
        sta = User_status.objects.create(status=s)
        book.status = sta
        book.save()
        error = True
    d = {'book' : book, 'error' : error}
    return render(request, 'assign_user_status.html', d)
