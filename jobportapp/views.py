from django.shortcuts import render, redirect
from .forms import Profilereg, Clgreg
from .models import profile


# Create your views here.


def index(request):
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
    return render(request,'index.html',{'form':fm})
    
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
        
 
        