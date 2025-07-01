from django.shortcuts import render
from .models import bioData
from .models import exp, project
from django.http import HttpResponse, HttpResponseRedirect
from dotenv import load_dotenv
import os
load_dotenv()
# Create your views here.
login=False
def homepage(request):
    data=bioData.objects.get(istrue=True)
    proj=project.objects.filter(role=data.role)
    exper=exp.objects.filter(role=data.role)
    return render(request,"index.html",{'data':data, 'proj':proj, 'exper':exper })

def login(request):
    return render(request,"login.html")

def biodata(request):
    if(request.session.get('islog')==True):
        return render(request,'admin.html')
    else:
        return HttpResponseRedirect('/login')
def projectpage(request):
    if(request.session.get('islog')==True):
        return render(request, "project.html")
    else:
        return HttpResponseRedirect('/login')

def experince(request):
    if(request.session.get('islog')==True):
        return render(request, 'exp.html')
    else:
        return  HttpResponseRedirect('/login')
def signIn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # if(request.session.get('islog')==True):
        #     return render(request, "admin.html")
        if(username==os.getenv('username1') and password==os.getenv('password1')):
            request.session['islog']=True
            return render(request, "admin.html")
        else:
            msg="username or password is wrong"
            return render(request, "login.html",{"msg":msg})
        
    else:
        return render(request,"login.html")

def fillBiodata(request):
    if request.method=='POST':
        key=request.POST['key']
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        linkdin=request.POST['linkdin']
        contact=request.POST['contact']
        gitlink=request.POST['gitlink']
        leetcode=request.POST['leetcode']
        role=request.POST['role']
        istrue=False
        if(request.POST['istrue']=='true'):
            istrue=True
        bioData(key=key, name=name, dob=dob, linkdin=linkdin, contact=contact, gitlink=gitlink,leetcodelink=leetcode, email=email, role=role, istrue=istrue).save()
        return render(request, 'admin.html')
    else:
        return render(request, 'baseAdmin.html')
    
def fillexp(request):
    if request.method=='POST':
        role=request.POST['role']
        key=request.POST['key']
        title=request.POST['title']
        desc=request.POST['desc']
        cred=request.POST['cred']
        exp(key=key,title=title, desc=desc, cred=cred, role=role).save()
        return render(request, 'exp.html',{'msg':"data saved success."})
    else:
        return render(request,'exp.html',{'msg':'data not save'})
def fillproject(request):
    if request.method=='POST':
        role=request.POST['role']
        image=request.POST['image']
        prjurl=request.POST['prj']
        title=request.POST['title']
        project(image=image, prjurl=prjurl, title=title, role=role).save()
        return render(request, 'project.html', {'msg':'yes data saved'})
    else:
        return render(request, 'project.html',{'msg':'data not saved'})

