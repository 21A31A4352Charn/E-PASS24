from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import student,Reports,prof
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from .mail import mails
from django.shortcuts import reverse



# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("Password")
        print(username,password)
        user = authenticate(username=username, password=password)
        pattern = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        if pattern.search(username) is not None:
            messages.info(request,"if you are an admin please login in admin page")
            return render(request, 'login.html')
            
        if user is not None:
                login_user(request,user)
                return redirect('user')
        else:
                messages.success(request,"please check you cradentials")
                return render(request, 'login.html')

    else:
        return render(request,'login.html')


def anew(request):
    if request.method=="POST" and request.FILES['photos']:
        username=request.POST.get("Rollnumber")
        name=request.POST.get("name")
        branch=request.POST.get("branch")
        photo=request.FILES['photos']
        ps=FileSystemStorage()
        image=ps.save(photo.name,photo)
        uploaded_file_url = ps.url(image)
        password=request.POST.get("password")
        user=User.objects.create_user(username=username,first_name=name,last_name=branch,email=username,password=password)
        user.save()
        sp=prof(username=username,photo=uploaded_file_url)
        sp.save()
        return redirect(ads)
    else:
        return render(request, 'new.html')
    if request.method == 'POST':
        # Handle form submission here
        return redirect(reverse('login'))


def home(request):
    if request.method=="POST" and request.FILES['photo']:
        username=request.POST.get("Rollnumber")
        name=request.POST.get("Name")
        branch=request.POST.get("Branch")
        section=request.POST.get("Section")
        year=request.POST.get("year")
        email=request.POST.get("email")
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        image=fs.save(photo.name,photo)
        uploaded_file_url = fs.url(image)
        password=request.POST.get("password")
        user=User.objects.create_user(username=username,first_name=name,last_name=branch,email=email,password=password)
        user.save()
        sp=student(username=username,section=section,year=year,photo=uploaded_file_url)
        sp.save()
        messages.success(request, 'Data saved successfully')
        return render(request,'signin.html')
    else:
        return render(request,'signin.html')
    if request.method == 'POST':
        # Handle form submission here
        return redirect(reverse('login'))

@login_required(login_url='/')
def user(request):
    u=request.user.username
    H = student.objects.filter(username=u)
    user = User.objects.filter(username=u)
    print(H.values_list())
    context = {'data': zip(H,user),'b':user}
    return render(request, 'user.html',context)


@login_required(login_url='/')
def reports(request):
    if request.method=="POST":
        username=request.user.username
        branch=request.user.last_name
        date=request.POST.get('date')
        subject=request.POST.get('reason')
        reports=request.POST.get('reasons')
        r=Reports(username=username,branch=branch,date=date,subject=subject,reason=reports)
        r.save()
        u=request.user.username
        H = student.objects.filter(username=u)
        user = User.objects.filter(username=u)
        H.nots=False
        context = {'data': zip(H,user)}
        messages.info(request,"You are request has sussesfully sent")
        return render(request, 'user.html',context)
    else:
        u=request.user.username
        H = student.objects.filter(username=u)
        user = User.objects.filter(username=u)
        context = {'data': zip(H,user)}
        return render(request,'user.html',context)
    

@login_required(login_url='/')
def logout(request):
    if request.method=="POST":
        logout_user(request)
        return redirect('login')


@login_required(login_url='/')
def inbox(request):
    if request.method=="POST":
        u=request.user.username
        k = student.objects.filter(username=u)
        user = User.objects.filter(username=u)
        context = {'data': zip(k,user)}
        H = student.objects.get(username=u)
        if H.nots==True:
            if H.nots==True and H.accept==True:
                return render(request,'information.html',context)
            elif  H.nots==True and H.declane==True:
                return render(request,'notinform.html',context)
            else:
                return redirect('user')
        else:
            return redirect('user')
    else:
        u=request.user.username
        H = student.objects.filter(username=u)
        user = User.objects.filter(username=u)
        context = {'data': zip(H,user)}
        return render(request,'information.html',context)

@login_required(login_url='/')
def notifications(request):
    u=request.user.username
    H = prof.objects.filter(username=u)
    print(H.values_list())
    user = User.objects.filter(username=u)
    n=Reports.objects.all()
    context = {'data': zip(H,user),'notees':n}
    return render(request, 'interface.html',context)


@login_required(login_url='/')
def open(request):
    if request.method=="POST":
        rollnumber=request.POST.get('rollnumber')
        H = student.objects.filter(username=rollnumber)
        user = User.objects.filter(username=rollnumber)
        n=Reports.objects.filter(username=rollnumber)
        print(H,n,user)
        context = {'data': zip(H,user),'report':zip(user,n)}
        return render(request,'mains.html',context)


@login_required(login_url='/')  
def decline(request):
    if request.method=="POST":
        rollnumber=request.POST.get('rollnumber')
        R = Reports.objects.filter(username=rollnumber)
        H = student.objects.get(username=rollnumber)
        user = User.objects.filter(username=rollnumber)
        emails=user.values_list()[0][7]
        H.declane=True
        H.nots=True
        H.save()
        R.delete()
        #mails(emails,"Your permission was accpted \nFor further information please check your profile")
        return redirect('notifictions')


@login_required(login_url='/')
def accept(request):
    if request.method=="POST":
        rollnumber=request.POST.get('rollnumber')
        H = student.objects.get(username=rollnumber)
        R = Reports.objects.get(username=rollnumber)
        user = User.objects.filter(username=rollnumber)
        emails=user.values_list()[0][7]
        H.accept=True
        H.nots=True
        H.save()
        R.delete()
        #mails(emails,"Your permission was accpted \nFor further information please check your profile")
        return redirect('notifictions')


def ads(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("Password")
        print(username,password)
        user = authenticate(username=username, password=password)
        pattern = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        if pattern.search(username) is not None:
            if user is not None:
                login_user(request,user)
                return redirect('notifictions')
            else:
                return render(request, 'adminsss.html')
        else:
            return render(request, 'adminsss.html')
    else:
        return render(request,'adminsss.html')
