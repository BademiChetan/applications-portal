from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import inlineformset_factory
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from portal.models import *
from django.shortcuts import *
from django import forms
from forms import *
from django.http import *

# Create your views here.

def log_out(request):
    logout(request)
    return HttpResponse('You have been Logged Out successfully.<a href="/">Home</a>')
    
            
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            inputs = form.cleaned_data
            new_user = User(first_name=inputs['name'],username=inputs['username'],email=inputs['email'])
            new_user.set_password(inputs['password'])
            new_user.save()
            new_user = authenticate(username=inputs['username'],password=inputs['password'])
            login(request, new_user)
            new_profile=UserProfile(user=User.objects.get(username=request.POST['username']),rollno=request.POST['rollnumber'],hostel=request.POST['hostel'],ph_no=request.POST['phoneno'],room_number=request.POST['room_number'],cgpa=request.POST['cgpa'])
            new_profile.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('Register.html',locals(),context_instance=RequestContext(request))


def home(request):
    """
    Home Page of Application Portal. Also has login. Part 1
    checks if user is already logged in and then redirects
    to the corresponding page. Part 2 is for logging in.

    """
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return HttpResponseRedirect("/super_home")
        else: 
            curr_user= UserProfile.objects.get(user=request.user)
            if curr_user.is_core==False:
                return HttpResponseRedirect("/coord_home")
            else:
                return HttpResponseRedirect("/core_home")  

    if(request.method=='POST'):
        form = Loginform(request.POST)
        if form.is_valid():
            inputs = form.cleaned_data
            user = authenticate(username=inputs['username'],password=inputs['password'])
            if user is not None:
                login(request, user)
                print request.user
                if request.user.is_superuser:
                    return HttpResponseRedirect("/super_home")
                else:    
                    curr_user = UserProfile.objects.get(user=request.user)
                    if curr_user.is_core==False:
                        return HttpResponseRedirect("/coord_home")
                    else:
                        return HttpResponseRedirect("/core_home/")
            else:                
                return render_to_response("Invalid.html",locals(),context_instance=RequestContext(request))               
    else:
        form = Loginform()
    return render_to_response("Home.html",locals(),context_instance=RequestContext(request))


def super_home(request):
    """
    To display super user's home page.  This page will have tables of core details and groups.
    The super user can add/edit a group and its permissions
 
    """
    if request.user.is_authenticated() is not True or request.user.is_superuser is not True:
        return HttpResponseRedirect('/')
    if(request.method=='POST'):
        try:
            request.POST['Add']
        except:
            try:
                temp=request.POST['Edit']
            except:
                temp=request.POST['Del']
                return HttpResponseRedirect('/delgroup/'+temp)
            return HttpResponseRedirect('/editgroup/'+temp)
        if(request.POST['Add']=="Add"):
            return HttpResponseRedirect('/addgroup')
        return HttpResponseRedirect('/addcore/'+request.POST['Add'])
    grp=[]
    cores=[]
    groups=Group.objects.all()
    for g in groups:
        grp.append(g.name)
        members=User.objects.filter(groups=g)
        core=[]
        links=[]
        for m in members:
            u=UserProfile.objects.get(user=m)
            if(u.is_core==True):
                core.append(m)
                link="/editcore/"+str(m.id)
                links.append(link)
        cores.append(zip(core,links))
    data=zip(grp,cores)
    return render_to_response('super_home.html',locals(),context_instance= RequestContext(request))


def addgroup(request):
    """
    Adds a group through the addgroup form to the Group Model 

    """
    if request.method == 'POST':
        form = AddGroup(request.POST)
        if form.is_valid():
            new_group = form.save()
            return HttpResponseRedirect('/super_home/')
        else:
            return HttpResponse('Group name unavailable! <a href="/addgroup">Back</a>')
            
    else:
        form = AddGroup()
        return render_to_response('addgroup.html',{'form':form,},context_instance=RequestContext(request))

   
def editgroup(request,temp):
    """
    Edits group name and permissions of a particular group

    """
    gedit=Group.objects.get(name=temp)   
    if request.method == 'POST':
        form = AddGroup(request.POST, instance=gedit)
        if form.is_valid():
            group = form.save()
            return HttpResponseRedirect('/super_home/')
        else:
            return HttpResponse('Error')
            
    else:
        form = AddGroup(instance=gedit)
        return render_to_response('editgroup.html',{'form':form,},context_instance=RequestContext(request))


def delgroup(request,temp):
    """ 
    Deletes a group from the Group table 
 
    """
    grouptodel=Group.objects.get(name=temp)
    corestodel=User.objects.filter(groups=grouptodel)
    for core in corestodel:
        profile=UserProfile.objects.get(user=core)
        profile.delete()
        core.delete()
    grouptodel.delete()
    return HttpResponse('Group has been deleted successfully.<a href="/">Home</a>')


def addcore(request,temp):
    """
    Adds cores into a group

    """
    grp=Group.objects.get(name=temp)
    if request.method == 'POST':
        form = AddCore(request.POST)
        if form.is_valid():
            inputs = form.cleaned_data
            new_user = User(first_name=inputs['name'],username=inputs['username'],email=inputs['email'])
            new_user.set_password(inputs['password'])
            try:
                new_user.save()
            except:
                return HttpResponse('Username is not available.<a href='+"/addcore/"+str(temp)+'>Back</a>')
            new_user.groups.add(grp)
            new_user.save()
            new_user = authenticate(username=inputs['username'],password=inputs['password'])
            return HttpResponseRedirect('/coredetails/'+ str(new_user.id))
    else:
        form = AddCore()
    return render_to_response('addcore.html',{'form':form,},context_instance=RequestContext(request))


def coredetails(request, id1):
    """
    To save user profile details

    """
    user=User.objects.get(id=id1)
    if request.method == 'POST':
        form = CoreUserProfile(request.POST)
        if form.is_valid(): 
            new_core = form.save()
            return HttpResponseRedirect('/super_home/')
        else:
            return HttpResponse('Error')
            
    else:
        form = CoreUserProfile(initial={'user':user, 'is_core':True})
        return render_to_response('addcore.html',{'form':form},context_instance=RequestContext(request)) 

def editcore(request,id1):
    return HttpResponse('Edit Core Page')
