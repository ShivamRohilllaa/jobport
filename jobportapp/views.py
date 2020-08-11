from django.shortcuts import render, redirect, HttpResponse
from .forms import Profilereg, Clgreg
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Profdet(request):
    if request.method == 'POST':
        fm = Profilereg(request.POST)
        if  fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            address = fm.cleaned_data['address']
            reg = profile(name=name, email=email, phone=phone, address=address)
            reg.save()
            # It refresh the form and show the form empty
            fm = Profilereg() 
            return redirect('/clgdet')
    else:
        fm = Profilereg()
    # show = profile.objects.all()      
    return render(request,'profile.html',{'form':fm})
    
def clgdet(request):
    if request.method == 'POST':
        om = Clgreg(request.POST)
        if  om.is_valid():
            college = om.cleaned_data['college']
            school = om.cleaned_data['school']
            branch = om.cleaned_data['branch']
            degree = om.cleaned_data['degree']
            clgreg = clgdet(college=college, school=school, branch=branch, degree=degree)
            clgreg.save()
            # It refresh the form and show the form empty
            om = Clgreg() 
    else:
        om = Clgreg()
    show = profile.objects.all()    
    return render(request,'clgdet.html',{'form':om, 'show':show})

def index(request):
    return render(request, 'index.html')

def update_data(request, id):
    if request.method == 'POST':
        edit = profile.objects.get(pk=id)
        fm = Profilereg(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
            return redirect('/clgdet')
    else:
        edit = profile.objects.get(pk=id)
        fm = Profilereg(instance=edit)
    return render(request, 'profupdate.html', {'form':fm})
    
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request,'Password do not match')
            return render('home')

    #Create the users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.Last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been Successfully Created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')      

def handleLogin(request):
    loginusername = request.POST['loginusername']        
    loginpassword = request.POST['loginpassword']

    user = authenticate(username= loginusername, password= loginpassword)
    if user is not None:
        login(request, user)
        messages.success(request, "You are successfully logged in")
        return redirect('/profdet')

    else:
        messages.error(request, "Please Enter Correct Username & Password")
        return redirect('home')

def handleLogout(request):
    logout(request)
    messages.success(request, "You are logged Out")
    return redirect('home')       