from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from.models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_view(request):
    return render(request,'home.html')
    return redirect("login")
    return redirect("dashboard")
    return redirect("register")

def registration(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        password = request.POST.get('phone')
        phone = request.POST.get('phone')
        username = request.POST.get('email')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        streetAddress = request.POST.get('streetAddress')
        city = request.POST.get('city')
        region = request.POST.get('region')
        district = request.POST.get('district')
        country = request.POST.get('country')
        previousSchool = request.POST.get('previousSchool')
        gpa = request.POST.get('gpa')
        programOfInterest= request.POST.get('programOfInterest')
        sop = request.POST.get('sop')
        emergencyName = request.POST.get('emergencyName')
        emergencyPhone = request.POST.get('emergencyPhone')

        user = User.objects.create_user(username=email, email=email, password=password)

        student = Student.objects.create(
                            user=user,
                            fullName=fullName, 
                            phone=phone, 
                            email=email, 
                            dob=dob,
                            gender=gender,
                            streetAddress=streetAddress, 
                            city=city, 
                            region=region, 
                            district=district, 
                            country=country, 
                            previousSchool=previousSchool, 
                            gpa=gpa, 
                            programOfInterest=programOfInterest, 
                            sop=sop, 
                            emergencyName=emergencyName,
                            emergencyPhone=emergencyPhone)
    
    return render(request, "register.html")



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'login.html',{'error':'invalid username or password'})
    return render(request, 'login.html')
    return redirect("register")


def dash_board_view(request):
    student = Student.objects.get(user=request.user)
    return render(request, "dashboard.html", {"student": student})

def updateSTUinfo(request):
    if request.method == 'POST':
        user = request.user
        fullName = request.POST.get('fullName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        emergencyName = request.POST.get('emergencyName')
        emergencyPhone = request.POST.get('emergencyPhone')
        user.save()

        return redirect('dashboard')
    return render(request, "updateSTUinfo.html")


def logout_page(request):
    logout(request)
    return redirect('login')