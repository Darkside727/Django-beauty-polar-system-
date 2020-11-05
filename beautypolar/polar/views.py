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
        user = authenticate(username = email, password=password)
        try:
            regis = registration.objects.get(user = user)     #User Login
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
  return redirect("View_user")                    # remove user


def View_new_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')                   # requested user
    status = User_status.objects.get(status="Pending")
    pro = registration.objects.filter(status=status)
    d = {'user' : pro}
    return render(request, 'request_user.html', d)


def Assign_user_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = False
    book = registration.objects.get(id=pid)               # assign Status to the user
    if request.method == "POST":
        n = request.POST['book']
        s = request.POST['status']
        username = User.objects.get(username=n)
        book.user = username
        sta = User_status.objects.create(status=s)
        book.status = sta
        book.save()
        error = True
    d = {'book' : book, 'error' : error}
    return render(request, 'assign_user_status.html', d)


# def Assign_book_status(request, pid):
#     if not request.user.is_authenticated:
#         return redirect('admin_login')
#     error = False
#     book = Apponitment.objects.get(id=pid)
#     if request.method == "POST":                           #assign Booking Status
#         n = request.POST["book"]
#         s = request.POST["status"]
#         username = User.objects.get(username=n)
#         cust  = registration.objects.get(user= username)
#         book.registration = cust
#         sta = User_status.objects.create(status = s)
#         book.status = sta
#         book.save()
#     d = {'book' : book , 'error' : error}
#     return render(request, 'assgin_status.html', d)


def View_appoiment_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    pro = Apponitment.objects.all()    # Admin site Function view All appoimet
    messge = {'user' : pro}
    return render(request, 'all_apoiments.html', messge)


def View_new_appoiments(request):
    if not request.user.is_authenticated:
       return redirect('admin_login')                   # requested user
    status = BookStatus.objects.create(status="pending")
    pro = Apponitment.objects.filter(status=status)
    print(pro)
    d = {'user' : pro}
    return render(request, 'requested_appoiment.html', d)


def View_Confrim_Appointement(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    status = User_status.objects.get(status="Accept")
    pro = Apponitment.objects.filter(status = status)
    d = {'appoint' : pro}
    return render(request, 'confrim_appo.html', d)


def view_Services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    pro = Service.objects.all()
    d = {"service" : pro}
    return render(request, 'view_Services.html', d)


def Add_service(request):
    error = False
    if request.method == "POST":
        s = request.POST['service']
        c = request.POST['cost']
        desc = request.POST['desc']
        i = request.FILES['files']
        ser = Service.objects.create(image=i, cost= c , name = s, decs=desc)
        error = True
    d = {'error' : error}
    return render(request, 'add_services.html', d)


def profile(request):
    user = User.objects.get(id = request.user.id)
    pro = registration.objects.get(user=user)
    d = {'pro' : pro}
    return render(request, 'profile.html', d)


def Edit_profile(request):
    user = User.objects.get(id=request.user.id)
    print(user)
    pro = registration.objects.get(user=user)
    error = False
    if request.method == "POST":
        f = request.POST["fname"]
        l = request.POST["lname"]
        u = request.POST["contact"]
        try:
            i = request.FILES['image']
            pro.image = i
            pro.save()
        except:
            pass
        user.first_name = f
        user.last_name = l
        pro.contact = u
        user.save()
        pro.save()
        error = True
    d = {'error' : error, "pro" : pro}
    return render(request, 'edit_profile.html', d)


def All_services(request):
    user = Service.objects.all()
    d = {"pro": user}
    return render(request, 'all_services.html', d)


def Book_appointment(request):
    user  = User.objects.get(id=request.user.id)
    pro = registration.objects.get(user=user)
    service = Service.objects.all()
    error = False
    if request.method == "POST":
        s = request.POST["service"]
        t = request.POST["time"]
        d = request.POST["date"]
        stat = BookStatus.objects.create(status="Pending")
        print(stat)
        paid = BookPaid.objects.create(paid="NotPaid")
        serv = Service.objects.get(name=s)
        Apponitment.objects.create(paid = paid, customer=pro, date1=d, time1=t, service=serv, status=stat)
        error = True
    d = {"error": error, 'pro': pro, 'service': service}
    return render(request, "book_appoin.html", d)


def View_appoiments(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')                   # requested user appoiments
    user = User.objects.get(id=request.user.id)
    pro =  registration.objects.get(user=user)
    appoi = Apponitment.objects.filter(customer=pro).all()
    d = {'user' : appoi}
    return render(request, 'my_appoitment.html', d)


def del_appoiments(request, pid):
    data = Apponitment.objects.get(id=pid)
    data.delete()
    if request.user.is_staff:
        return redirect('View_appoiment_all')
    else:
        return redirect('View_appoiments')


def book_selected_appoitment(request, pid):
    user  = User.objects.get(id=request.user.id)
    pro = registration.objects.get(user = user)
    book = Service.objects.get(id=pid)
    error = False
    print("Come")
    if request.method == "POST":
       s = request.POST["service"]
       t = request.POST["time"]
       d = request.POST["date"]
       stat = BookStatus.objects.get(b_status="Pending")
       paid = BookPaid.objects.get(paid="NotPaid")
       serv = Service.objects.get(name=s)
       Apponitment.objects.create(paid = paid, customer=pro, date1=d, time1=t, service=serv, status=stat)
       error = True
    d = {"error": error, 'pro': pro, 'book': book}
    return render(request, 'book_selected_appoitment.html', d )
