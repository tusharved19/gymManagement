from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    enquiry=Enquiry.objects.all()
    member=Member.objects.all()
    equipment=Equipment.objects.all()
    plan=Plan.objects.all()
    e1 = 0
    p1 = 0
    eq1 = 0
    m1 = 0
    for i in enquiry:
        e1 += 1
    for i in member:
        m1 += 1
    for i in equipment:
        eq1 += 1
    for i in plan:
        p1 += 1
    d = {'e1': e1,'m1': m1,'eq1': eq1,'p1': p1}
    return render(request,'index.html',d)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    d = {'error': error}
    return render(request,'login.html', d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Add(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n = request.POST['Name']
        c = request.POST['Contact']
        e = request.POST['EmailID']
        a = request.POST['Age']
        g = request.POST['Gender']
        try:
            Enquiry.objects.create(Name=n,Contact=c,EmailID=e,Age=a,Gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add.html', d)

def View(request):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    d = {'enq':enq}
    return render(request,'view.html', d)

def Delete_Enquiry(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view')

def Aequip(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        de = request.POST['description']
        try:
            Equipment.objects.create(name=n,price=p,unit=u,date=d,description=de)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'aequip.html', d)

def Vequip(request):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.all()
    d = {'equipment':equipment}
    return render(request,'vequip.html', d)

def DeleteEquipment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('vequip')


def Aplan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create(name=n,amount=a,duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'aplan.html', d)

def Vplan(request):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.all()
    d = {'plan':plan}
    return render(request,'vplan.html', d)

def Deleteplan(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('vplan')

def Amember(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    plan1 = Plan.objects.all()
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        j = request.POST['joindate']
        ex = request.POST['expiredate']
        i = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        
        try:
            Member.objects.create(name=n,contact=c,emailid=e,age=a,gender=g,plan=plan,joindate=j,expiredate=ex,initialamount=i)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'plan':plan1}
    return render(request, 'amember.html', d)

def Vmember(request):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.all()
    d = {'member':member}
    return render(request,'vmember.html', d)

def Deletemember(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('vmember')





