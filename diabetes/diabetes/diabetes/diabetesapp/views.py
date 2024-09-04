from django.shortcuts import redirect, render
from . models import user,feedback

# Create your views here.
def index(request):
    return render (request,'index.html')

def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        contact=request.POST.get('contact')
        mail=request.POST.get('mail')
        password=request.POST.get('password')

        user(username=username,contact=contact,mail=mail,password=password).save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=user.objects.filter(username=username,password=password)
        if cr:
            userd=user.objects.get(username=username,password=password)
            id=userd.id
            username=userd.username
            password=userd.password
            request.session['id']=id
            request.session['username']=username
            request.session['password']=password
            return  redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')    

def profile(request):
    username=request.session['username']
    cr=user.objects.get(username=username)
    if cr:
        user_info={
            'username':cr.username,
            'contact':cr.contact,
            'mail':cr.mail,
            'password':cr.password,
        }
        return render(request,'profile.html',user_info)
    else :
        return render(request,'profile.html')


def updatepro(request):
    username=request.session['username']
    cr=user.objects.get(username=username)
    if cr:
        user_info={
            'username':cr.username,
            'contact':cr.contact,
            'mail':cr.mail,
            'password':cr.password,
        }
        return render(request,'updatepro.html',user_info)
    else :
        return render(request,'updatepro.html')


def pro_update(request):
    username=request.session['username']
    if request.method=="POST":
        username=request.POST.get('usernametxt')
        contact=request.POST.get('contacttxt')
        mail=request.POST.get('mailtxt')
        password=request.POST.get('passwordtxt')

        data=user.objects.get(username=username)
        data.username=username
        data.contact=contact
        data.mail=mail
        data.password=password
        data.save()
        return redirect('profile')
    else:
        return render(request,'updatepro.html')

def feedbacks(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone') 
        email=request.POST.get('mail')
        message=request.POST.get('message')

        feedback(username=name,contact=phone,mail=email,message=message).save()
        return render(request,'index.html')
    else:
        return render(request,'feedback.html')
    


def home(request):
    return render (request,'home.html')
def logout(request):
    return render (request,'index.html')


def adlog(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        u='admin'
        p='admin'
        if username==u:
            if password==p:
                return render(request,'adhome.html')
            else:
                return render(request,'adlogin.html')
        else:
            return render(request,'adlogin.html')
    else:
        return render(request,'adlogin.html')        
    

def aduser(request):
    a=user.objects.all()
    return render(request,'aduser.html',{'a':a})

def adfeedback(request):
    a=feedback.objects.all()
    return render(request,'aduser.html',{'a':a})
def feedremove(request,id):
    a=feedback.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html',{'a':a})
def useremove(request,id):
    a=user.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html',{'a':a})

def docreg(request):
    if request.method=="POST":
        doctorname=request.POST.get('doctorname')
        qualification=request.POST.get('qualification') 
        department=request.POST.get('department')
        hospitalname=request.POST.get('hospitalname')
        experience=request.POST.get('experience') 
        consultingtime=request.POST.get('consultingtime')
        place=request.POST.get('place')
        fee=request.POST.get('fee') 
        email=request.POST.get('email')
        password=request.POST.get('password')



        feedback(doctorname=doctorname,contact=phone,mail=email,message=message).save()
        return render(request,'index.html')
    else:
        return render(request,'feedback.html')
    
