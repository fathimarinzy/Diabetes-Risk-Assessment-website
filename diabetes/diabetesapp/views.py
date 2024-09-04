from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import user,feedback,Info,doctor,appointments
from django.http import HttpResponse
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import smtplib
from django.core.mail import send_mail
from django.http import Http404
import smtplib


# Create your views here.
def index(request):
    return render (request,'index.html')

def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        contact=request.POST.get('contact')
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        try:
           validate_password(password,user)
        except ValidationError as e:
            return render(request,'register.html',{'error_message':e}) 
        user(username=username,contact=contact,mail=mail,password=password).save()
        alert_message ="<script>alert('Registration Successful!');window.location.href='/login';</script>"
        #return the alert message
        return HttpResponse(alert_message)
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    error_message = None
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
            error_message ="Invalid Username or Password. Please try again."
            return render(request,'login.html',{'error_message':error_message})
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
        alert_message ="<script>alert('Feedback Submitted!');window.location.href='/home';</script>"
        #return the alert message
        return HttpResponse(alert_message)
        return render(request,'home.html')
    else:
        return render(request,'feedback.html')
    


def home(request):
    return render (request,'home.html')
def adhome(request):
    return render(request,'adhome.html')
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
    return render(request,'adfeedback.html',{'a':a})
def feedremove(request,id):
    a=feedback.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html')
def useremove(request,id):
    a=user.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html')

# def contact(request):
#     return render (request,'contact.html')


from .models import Info
# from django.shortcuts import render
# import pandas as pd 
# from sklearn.linear_model import LogisticRegression  # type: ignore
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score 

# # Load the model
# model = LogisticRegression()
# model.load('path_to_your_model_file') 

def info(request):
    if request.method == "POST":
        # Extract data from the POST request
        pregnancies = int(request.POST.get('Pregnancies'))
        glucose = int(request.POST.get('Glucose')) 
        bloodpressure = int(request.POST.get('Bloodpressure'))
        skinthickness = int(request.POST.get('Skinthickness'))
        gender = request.POST.get('gender', '')
        insulin = int(request.POST.get('Insulin'))
        bmi = float(request.POST.get('BMI'))
        diabetespedigreefunction = float(request.POST.get('Diabetespedigreefunction'))
        age = int(request.POST.get('Age'))

        # Save user information
        Info.objects.create(Pregnancies=pregnancies, Glucose=glucose, Bloodpressure=bloodpressure,
                            Skinthickness=skinthickness, Insulin=insulin, BMI=bmi,
                            Diabetespedigreefunction=diabetespedigreefunction, Age=age, gender=gender)

        # Logic to determine if user has diabetes
        has_diabetes = glucose >= 126 or insulin >= 200 or bmi >= 30 or age > 45 or skinthickness >= 25 or pregnancies >= 4
        # Logic to determine if user has not diabetes
        does_not_have_diabetes = glucose < 126 and insulin < 200 and bmi < 30 and age <= 45 and skinthickness < 25 and pregnancies < 4


        # Prepare context data to pass to template
        context = {'has_diabetes': has_diabetes}
        context = {'does_not_have_diabetes': does_not_have_diabetes }

        if has_diabetes:
            # Provide some tips and remedies if the user has diabetes
            tips_and_remedies = "Follow a balanced diet, exercise regularly, monitor blood sugar levels, and consult with a healthcare professional for personalized advice."
            context['tips_and_remedies'] = tips_and_remedies

        # Render the result template with context data
        return render(request, 'result.html', context)
    else:
        # If the request method is not POST, render the info.html template
        return render(request, 'info.html')

def adinfo(request):
    a=Info.objects.all()
    return render (request,'adinfo.html',{'a':a})
def inforemove(request,id):
    a=Info.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html',{'a':a})

def docreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        qualification=request.POST.get('qualification') 
        department=request.POST.get('department')
        hname=request.POST.get('hname')
        experience=request.POST.get('experience')
        ctime=request.POST.get('ctime')
        place=request.POST.get('place')
        fee=request.POST.get('fee')
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
           validate_password(password,doctor)
        except ValidationError as e:
            return render(request,'docreg.html',{'error_message':e})
     
        doctor(name=name,qualification=qualification,department=department,hname=hname,experience=experience,ctime=ctime,place=place,fee=fee,email=email,password=password).save()
        alert_message ="<script>alert('Registration Successful!');window.location.href='/doclog';</script>"
        #return the alert message
        return HttpResponse(alert_message)
        return render(request,'doclog.html')
    else:
      return render (request,'docreg.html')
    
def doclog(request):
    error_message = None
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        cr=doctor.objects.filter(name=name,password=password)
        if cr:
            userd=doctor.objects.get(name=name,password=password)
            id=userd.id
            name=userd.name
            password=userd.password
            request.session['id']=id
            request.session['name']=name
            request.session['password']=password
            return  redirect('dochome')
        else:
            error_message ="Invalid Username or Password. Please try again."
            return render(request,'dochome.html',{'error_message':error_message})
    else:
        return render(request,'doclog.html')    
    
def dochome(request):
    return render (request,'dochome.html')

def appointment(request,id):
    data=doctor.objects.get(id=id)
    name=data.name
    fee=data.fee
    hname=data.hname
    ctime=data.ctime
    username=request.session['username']
    cr=user.objects.get(username=username)
    username=cr.username
    contact=cr.contact
    mail=cr.mail
    return render(request,'appointment.html',{'name':name,'fee':fee,'hname':hname,'ctime':ctime,'username':username,'contact':contact,'mail':mail})
    alert_message ="<script>alert('Appointment Successful!');window.location.href='/home';</script>"
        #return the alert message
    return HttpResponse(alert_message)

def appsuccess(request):
    if request.method=="POST":
        name=request.POST.get('name')
        fee=request.POST.get('fee')
        contact=request.POST.get('contact')
        username=request.POST.get('username')
        date=request.POST.get('date')
        mail=request.POST.get('mail')
        hname=request.POST.get('hname')
        ctime=request.POST.get('ctime')
        p=appointments(name=name,fee=fee,contact=contact,hname=hname,ctime=ctime,username=username,date=date,mail=mail)
        p.save()
        return render(request,'appsuccess.html',{'name':name,'fee':fee,'username':username,'contact':contact,'hname':hname,'ctime':ctime,'date':date,'mail':mail})
        return render(request,'appointment.html',{'name':name,'fee':fee,'hname':hname,'ctime':ctime,'username':username,'contact':contact,'mail':mail})
        alert_message ="<script>alert('Appointment Successful!');window.location.href='/home';</script>"
        #return the alert message
        return HttpResponse(alert_message)
    else:
        return render(request,'appointment.html')
    
def doclist(request):
    d=doctor.objects.all()
    return render(request,'doclist.html',{'doc':d})

def dlist(request):
    d=doctor.objects.all()
    return render(request,'dlist.html',{'doc':d})

  

def ddelete(request,id):
    a=doctor.objects.get(id=id)
    a.delete()
    return render(request,'adhome.html')




def drpatient(request):
    name = request.session['name']
    data = appointments.objects.filter(name=name)
    print(data)
    return render(request,'drpatientlist.html',{'a':data})


def docpro(request):
    name=request.session['name']
    cr=doctor.objects.get(name=name)
    if cr:
        user_info={
            'name':cr.name,
            'qualification':cr.qualification,
            'department':cr.department,
            'hname':cr.hname,
            'experience':cr.experience,
            'ctime':cr.ctime,
            'place':cr.place,
            'fee':cr.fee,
            'email':cr.email,
            'password':cr.password,
        }
        return render(request,'docpro.html',user_info)
    else :
        return render(request,'docpro.html')


def docupd(request):
    name=request.session['name']
    cr=doctor.objects.get(name=name)
    if cr:
        user_info={
            'name':cr.name,
            'qualification':cr.qualification,
            'department':cr.department,
            'hname':cr.hname,
            'experience':cr.experience,
            'ctime':cr.ctime,
            'place':cr.place,
            'fee':cr.fee,
            'email':cr.email,
            'password':cr.password,
        }
        return render(request,'docupd.html',user_info)
    else :
        return render(request,'docupd.html')


def doc_update(request):
    name=request.session['name']
    if request.method=="POST":
        name=request.POST.get('name')
        qualification=request.POST.get('qualification')
        department=request.POST.get('department')
        hname=request.POST.get('hname')
        experience=request.POST.get('experience')
        ctime=request.POST.get('ctime')
        place=request.POST.get('place')
        fee=request.POST.get('fee')
        email=request.POST.get('email')
        password=request.POST.get('password')

        data=doctor.objects.get(name=name)
        data.name=name
        data.qualification=qualification
        data.department=department
        data.hname=hname
        data.experience=experience
        data.ctime=ctime
        data.place=place
        data.fee=fee
        data.email=email
        data.password=password
        data.save()
        return redirect('docpro')
    else:
        return render(request,'docupd.html')
    

def accept(request,id):
    data=appointments.objects.get(id=id)
    maill=data.mail
    print('email address',maill)
    print(maill)
    data.is_accepted = True
    data.save()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
    message = 'You Selected in Post Of HarithaKarmaSena Coordinater'
    s.sendmail("nefsal003@gmail.com",maill,message)
    s.quit()
    return render(request,'dochome.html')


# views
def output(request):
    return render(request,'output.html')

from django.shortcuts import render
from django.http import HttpResponse


API_URL = "https://api-inference.huggingface.co/models/shanover/symps_disease_bert_v3_c41"
headers = {"Authorization": "Bearer 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"}

from django.shortcuts import render
from django.http import HttpResponse
import requests

def get_disease_name(symptom):
    # Define a dictionary mapping specific symptoms to diseases
    disease_map = {
    "rashes with itching": "Fungal Infection",
    "fever": "Viral Infection",
    "cough": "Respiratory Infection",
    "sore throat": "Strep Throat",
    "headache": "Migraine",
    "nausea": "Gastritis",
    "vomiting": "Gastroenteritis",
    "diarrhea": "Food Poisoning",
    "fatigue": "Chronic Fatigue Syndrome",
    "muscle aches": "Fibromyalgia",
    "chest pain": "Heart Attack",
    "shortness of breath": "Asthma",
    "wheezing": "Bronchitis",
    "abdominal pain": "Appendicitis",
    "back pain": "Muscle Strain",
    "joint pain": "Arthritis",
    "swelling": "Edema",
    "itching": "Allergic Reaction",
    "runny nose": "Common Cold",
    "sneezing": "Allergic Rhinitis",
    "dizziness": "Vertigo",
    "numbness": "Neuropathy",
    "tingling": "Peripheral Neuropathy",
    "confusion": "Alzheimer's Disease",
    "memory loss": "Dementia",
    "difficulty concentrating": "Attention Deficit Disorder",
    "depression": "Major Depressive Disorder",
    "anxiety": "Generalized Anxiety Disorder",
    "panic attacks": "Panic Disorder",
    "insomnia": "Sleep Disorder",
    "snoring": "Sleep Apnea",
    "heartburn": "Gastroesophageal Reflux Disease",
    "indigestion": "Peptic Ulcer",
    "constipation": "Irritable Bowel Syndrome",
    "diarrhea": "Inflammatory Bowel Disease",
    "bloody stool": "Colon Cancer",
    "weight loss": "Hyperthyroidism",
    "weight gain": "Hypothyroidism",
    "excessive thirst,frequent urination,extreme hunger,unexplained weight loss,fatigue,blurred vision,slow healing infection": "Diabetes",
    "frequent urination": "Urinary Tract Infection",
    "burning sensation during urination": "Kidney Stones",
    "blood in urine": "Bladder Cancer",
    "difficulty swallowing": "Esophageal Cancer",
    "hoarseness": "Laryngeal Cancer",
    "sudden weight loss": "Pancreatic Cancer",
    "persistent cough": "Lung Cancer",
    "blood in sputum": "Tuberculosis",
    "unexplained fever": "Malaria",
    "muscle stiffness": "Lupus",
    "joint swelling": "Rheumatoid Arthritis",
    "joint deformities": "Osteoarthritis",
    "redness": "Cellulitis",
    "swollen lymph nodes": "Lymphoma",
    "night sweats": "HIV/AIDS",
    "enlarged spleen": "Mononucleosis",
    "headache": "Meningitis",
    "stiff neck": "Encephalitis",
    "blurred vision": "Glaucoma",
    "eye pain": "Corneal Abrasion",
    "double vision": "Multiple Sclerosis",
    "loss of peripheral vision": "Retinal Detachment",
    "vision loss": "Macular Degeneration",
    "ringing in ears": "Tinnitus",
    "hearing loss": "Ear Infection",
    "dizziness": "Meniere's Disease",
    "swollen glands": "Hypothyroidism",
    "excessive hunger": "Hyperglycemia",
    "frequent thirst": "Dehydration",
    "yellowing of skin": "Jaundice",
    "dark urine": "Hepatitis",
    "abdominal bloating": "Ovarian Cancer",
    "pelvic pain": "Endometriosis",
    "heavy menstrual bleeding": "Fibroids",
    "missed periods": "Polycystic Ovary Syndrome",
    "vaginal discharge": "Yeast Infection",
    "painful intercourse": "Pelvic Inflammatory Disease",
    "testicular pain": "Testicular Torsion",
    "scrotal swelling": "Epididymitis",
    "blood in semen": "Prostatitis",
    "erectile dysfunction": "Erectile Dysfunction",
    "painful urination": "Urethritis",
    "penile discharge": "Gonorrhea",
    "genital sores": "Genital Herpes",
    "vaginal itching": "Bacterial Vaginosis",
    "vaginal odor": "Trichomoniasis",
    "lower abdominal pain": "Chlamydia",
    "pain during intercourse": "Pelvic Inflammatory Disease",
    "painful periods": "Endometriosis",
    "irregular periods": "Polycystic Ovary Syndrome",
    "heavy periods": "Fibroids",
    "absence of periods": "Amenorrhea",
    "fertility problems": "Infertility",
        # Add more mappings as needed
    }
    # Check if the symptom has a specific mapping
    if symptom.lower() in disease_map:
        return disease_map[symptom.lower()]
    else:
        # If no specific mapping is found, return a default message
        return "No specific disease found for the given symptom"

def search(request):
    if request.method == 'POST':
        symptom = request.POST.get('symptom')

        if not symptom:
            return render(request, 'search.html', {'error': 'Input text is required'})

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": symptom})
            response_json = response.json()
            print("result---", response_json)
            print('##################')
            # Assuming response_json is a list of predictions
            predicted_diseases = [get_disease_name(symptom)]  # Pass the symptom to get_disease_name function
            print('new result', predicted_diseases)

            return render(request, 'output.html', {'predicted_diseases': predicted_diseases})
        
        except Exception as e:
            return render(request, 'search.html', {'error': str(e)})
    else:
        return render(request, 'search.html')
