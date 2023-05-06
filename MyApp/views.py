from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from LoginProject2 import settings
from django.core.mail import send_mail
from MyApp.models import Student
from MyApp.forms import StudentForm
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request,"MyApp/home.html")
def about(request):
    return render(request,"MyApp/About us.html")
def signin(request):
    return render(request,"MyApp/home.html")
def register(request):
    return render(request,"MyApp/register.html")
def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if User.objects.filter(username=username):
            messages.error(request,"Username already exits")
            return redirect("home")
        if User.objects.filter(email=email):
            messages.error(request,"Email already exits")
            return redirect("home")
        if len(username)>10:
            messages.error(request,"Your max len of username should be 10")
            return redirect("home")
        if pass2 != pass1:
            messages.error(request,"Both Passwords dont Match")
            return redirect("home")
        if  not username.isalnum():
            messages.error(request,"User name must be Alpha Numeric")
            return redirect("home")

        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been created sucessfully")
        #welcome Email
        subject="welcome to -Django login"
        message = "Hello welcome to django project \n we have sent a confirmation email, please confirm to Activate \n Thanking Hr Team "
        from_email= settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        return redirect("signin")
    return render(request,"MyApp/signup.html")

def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname= " Welcome to login page"
            return render(request,"MyApp/home.html")
        else:
            messages.error(request,"enter valid credentials")
            return redirect('home')

    return render(request,'MyApp/signin.html')


def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def success(request):
    return render(request,"MyApp/success.html")

def insert(request):
    if request.method=="POST":
        student_id=request.POST["student_id"]
        student_class=request.POST["student_class"]
        student_name=request.POST["student_name"]
        student_fathername=request.POST["student_fathername"]
        student_addr=request.POST["student_addr"]
        student_tuitionfee=request.POST["student_tuitionfee"]
        student_busfee = request.POST["student_busfee"]
        if Student.objects.filter(student_id=student_id):
            messages.error(request,"ID already exits")
            return redirect("/insert")
        my_stud=Student(student_id=student_id,student_class=student_class,student_name=student_name,student_fathername=student_fathername,student_addr=student_addr,student_tuitionfee=student_tuitionfee,student_busfee=student_busfee)
        my_stud.save()
        messages.success(request,"Added Successfully")
        return redirect("home")
    return render(request, "MyApp/insert.html")


def show_view(request):
    students=Student.objects.all()
    return render(request,"show.html",{"students":students})

def update(request,pk):
    student=Student.objects.get(id=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()

            return redirect('/show')
    return render(request,"MyApp/update.html",{"student":student})

from django.views.generic import ListView
from .models import Student

def listview(request):
    objects_list=Student.objects.all()
    return render(request,"MyApp/student_list.html",{"students":objects_list})

def delete_view(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    messages.success(request, "Added Successfully")
    return redirect('show')
def detail(request, pk):
    student = Student.objects.get(Student, student_name=id)
    return render(request, "MyApp/detail.html",{"student":student})
def due(request):
    return render(request,"MyApp/du.html")
def tuition_dues(request):
    students=Student.objects.filter(student_tuitionfee__gt=1000)
    return render(request, "MyApp/due.html", {"students": students})
def bus_dues(request):
    studentss=Student.objects.filter(student_busfee__gt=1000)
    return render(request, "MyApp/busfee.html", {"studentss": studentss})