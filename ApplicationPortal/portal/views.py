from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from portal.models import *
from django.shortcuts import *
from django import forms
from forms import *

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
    if(request.method=='POST'):
        try:
            request.POST['Add']=="Add"
        except:
            try:
                temp=request.POST['Edit']
            except:
                temp=request.POST['Del']
                return HttpResponseRedirect('/delgroup/'+temp)
            return HttpResponseRedirect('/editgroup/'+temp)
        return HttpResponseRedirect('/addgroup')
    grp=[]
    groups=Group.objects.all()
    for g in groups:
        grp.append(g.name)
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
            return HttpResponse('Group already exists! <a href="/">Home</a>')
            
    else:
        form = AddGroup()
        return render_to_response('addgroup.html',{'form':form,},context_instance=RequestContext(request))

   
def editgroup(request,temp):
    """
    Edits group name and permissions of a particular group

    """
    gedit=Group.objects.get(name=temp)   
    if request.method == 'POST':
        if request.POST['Submit']=='Add':
            return HttpResponseRedirect('/addcore/'+temp)            
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
            new_user.save()
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
        form = CoreUserProfile(initial={'user':user,})
        return render_to_response('addcore.html',{'form':form,},context_instance=RequestContext(request)) 





"""
#@Cores_Only
def core_question_add(request,idofevent,questionid=None):
    if request.method=='POST':
        event=Event.objects.get(Event.id=idofevent)
        question=request.POST['question']
        Question.objects.create(Question=question, event=event)
        added=True
        return render_to_response('addquestion.html', locals())
    
    event=Event.objects.get(Event.id=idofevent)
    if questionid is not None:
        added=False
        question=Question.objects.get(Question.id=questionid)  
        return render_to_response('addquestion.html',locals(),context_instance=RequestContext(request))          
    added = False
    return render_to_response('addquestion.html',locals(),context_instance=RequestContext(request))
    
#@Cores_Only
def core_question_add_existing(request,idofevent):
    all_questions=Question.objects.all()
    return render_to_response('viewquestion.html',locals(),context_instance=RequestContext(request))

  
@Cores_Only
def core_home(request):

    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    return render_to_response("home.html",{'user':user})  

def addevent(request):
    
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    p=user.group.event_set.all()
    if request.method=='POST':
        if request.POST.get('eventname',''):
            event=Event.create(name=request.POST.get('eventname'),group=user.group)
            p=user.group.event_set.all()
            return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))
        else:
            error=1 
            p=user.group.event_set.all()
            return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))   
    return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))
    
def editeventname(request,temp):
    e=Event.get(id=temp)
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    if request.method=='POST':
        if request.POST.get('eventname',''):
            e.name=request.POST.get('eventname')
            e.save()
        else:
            error=1 
            return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))   
    return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))
    user=UserProfile.objects.get(user=request.user)
    return render_to_response("home.html",{'user':user})    


@Coords_Only    
def coord_home(request):
    current="blah"
    if(request.method=='POST'):
            try:
                request.POST['save']
            except:
                choice=request.POST['choice']
                return render_to_response("answers.html",{'choice':choice})    
            return render_to_response("coord_home.html",{'user':current})    
    try:
        choiceset=Choice.objects.filter(user=request.user)
    except Exception:
        form=Preferenceform()
        return render_to_response("coord_home.html",{'user':current,'PreferenceForm':form,'choiceset':False})
    form.Preferenceform(initial = {'preference1':choiceset.objects.get(pref_no=1).event,'preference1':choiceset.objects.get(pref_no=2).event,'preference1':choiceset.objects.get(pref_no=3).event})
    return render_to_response("coord.html",{'user':current,'PreferenceForm':form,'choiceset':True})

    
@Cores_only        

        
def viewapplication(request, event_id, user_id):
    questions=Question.objects.filter(event.id=event_id)
    answers[]
    for q in questions:
        answers.append(Answer.objects.get(user.id=user_id, question=q))

    return render_to_response('view_application.html',locals(),context_instance= RequestContext(request))


@Cores_Only    
def viewevent(request,event_id):
    if request.method == 'POST':  
        if 'prefchoice' in request.POST:      
            pref_no = request.POST['preference']
            choice.Choice.objects.filter(pref_no=pref_no,event=event)
        if 'accept' in request.POST:
            pass
        if 'reject' in request.POST:
            pass#needs to be done. Accept values from checkbox
    return render_to_response("pref_choice.html",locals())    

def judgementday(request,eventid=None):
    events=Event.objects.all()
    if eventid is not None:
        event=Event.objects.get(Event.id=eventid)
        accepted=Choice.objects.filter(event.id=eventid, is_accepted=1)
        
    return render_to_response("final.html",locals()) 
def editquestion(request,questionid):
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    questionobj=Question.get(id=questionid)
    if request.method=='POST':
        if request.POST.get('content',''):
            questionobj.question=request.POST.get('content')
            return render_to_response("editquestion.html",locals(),context_instance=RequestContext(request))
        else:
            error=1
            return render_to_response("editquestion.html",locals(),context_instance=RequestContext(request))
    return render_to_response("editquestion.html",locals(),context_instance=RequestContext(request))
def deletequestion(request,questionid):
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    questionobj=Question.get(id=questionid)
    questionobj.delete()  
    return HttpResponse("Question Deleted")
"""
