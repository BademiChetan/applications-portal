from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from portal.models import *
from django.shortcuts import *
from django import forms
from forms import *
from django.db.models import Q

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
    for g in user.groups.all():
        group=g
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

def editcore(request, id1):
    """
    To edit details of cores or delete cores
    
    """
    user=User.objects.get(id=id1)
    core=UserProfile.objects.get(user=user)
    if request.method == 'POST':
        if request.POST['Submit']=='Del':
            user.delete()
            core.delete()
            return HttpResponse('Core has been deleted successfully.<a href="/">Home</a>')
        else:
            form1= AddCore(request.POST, initial={'name':user.first_name, 'username':user.username,'password':user.password,'confirm_password':user.password, 'email':user.email,} )
            form = CoreUserProfile(request.POST, instance=core)
            if form.is_valid(): 
                #Write code to Save form1 details
                user.first_name=request.POST['name']                
                user.username=request.POST['username']
                user.set_password(request.POST['password'])
                user.email=request.POST['email']
                user.save()
                form.save()
                return HttpResponseRedirect('/super_home/')
            else:
                return HttpResponse('Error')
            
    else:
        form1=AddCore(initial={'name' : user.first_name, 'username':user.username,'password':user.password, 'confirm_password':user.password, 'email':user.email,} )
        form = CoreUserProfile(instance=core)
        return render_to_response('editcore.html',{'form':form,'form1':form1,},context_instance=RequestContext(request)) 

#@Cores_Only
def core_home(request):
    group=[]
    temp=[]
    added=request.GET.get('added', None)
    deleted=request.GET.get('deleted', None)
    for g in Group.objects.all():
        if request.user in g.user_set.all():
            temp.append(g)
            event=Event.objects.filter(group=g)
            temp.append(event.all())
            group.append(temp)
            
    if request.method=='POST':
        event_delete=request.POST.getlist('event_delete')
        for i in event_delete:
                e=Event.objects.get(pk=i)
                qn=Question.objects.filter(event=e)
                for q in qn:
                    a=Answer.objects.filter(question=q)
                    a.delete()
                qn.delete()
                e.delete()
        html='/core_home/?deleted=True'
        return HttpResponseRedirect(html)
    return render_to_response("core_home.html",locals(),context_instance=RequestContext(request))

#@Cores_Only
def addevent(request,group_id):
    if request.method=='POST':
        if request.POST.get('eventname',''):
            group=Group.objects.get(pk=group_id)
            event=Event.objects.create(name=request.POST.get('eventname'), group=group)
            return HttpResponseRedirect('/core_home?added=1')
        else:
            error=1   
    return render_to_response("addevent.html",locals(),context_instance=RequestContext(request))

def question_clean(all_questions,question_list):
    #to remove questions that have already been added
    for q in question_list:
        all_questions=all_questions.filter(~Q(question=q.question))
        
    #to remove multiple copies of the same question
    question_compare=Question.objects.all()
    all_questions=list(all_questions)
    q_list=[]
    for p in question_compare:
        for q in all_questions:
            if q.question==p.question and q.event!=p.event:
                if q.id not in q_list:
                    all_questions.remove(q)
            elif q.question==p.question:
                q_list.append(q.id) 
                
    return all_questions

#@Cores_Only
def core_events(request,idofevent,questionid=None):
    exist = request.GET.get('exist', None)
    add = request.GET.get('add', None)
    edit_name = request.GET.get('edit_name', None)
    event_edited = request.GET.get('event_edited', None)
    edited = request.GET.get('edited', None)
    deleted = request.GET.get('deleted', None)
    event=Event.objects.get(pk=idofevent)
    question_list=Question.objects.filter(event=event)
    all_questions=Question.objects.all()
    all_questions=question_clean(all_questions,question_list)
            
    if request.method=='POST':
        if 'event_edit' in request.POST:
            event.name=request.POST['event_name']
            event.save()
            html='/core_home/events/%s/?event_edited=True' % idofevent
            return HttpResponseRedirect(html)
        if 'add' in request.POST:
            question=request.POST['question_new']
            q=Question.objects.create(question=question, event=event)
            added=True
            question_list=Question.objects.filter(event=event)
            all_questions=Question.objects.all()
            all_questions=question_clean(all_questions,question_list)
            return render_to_response('events.html', locals(),context_instance=RequestContext(request))

        if 'edit' in request.POST:
            question=Question.objects.get(pk=questionid)
            question.question=request.POST['question_edit']
            question.save()
            html='/core_home/events/%s/?edited=True' % idofevent
            return HttpResponseRedirect(html)

        if 'delete' in request.POST:
            qn_delete=request.POST.getlist('qn_delete')
            for i in qn_delete:
                qn=Question.objects.get(pk=i)
                for q in qn:
                    a=Answer.objects.filter(question=q)
                    a.delete()
                qn.delete()
            html='/core_home/events/%s/?deleted=True' % idofevent
            return HttpResponseRedirect(html)

        if 'select' in request.POST:
            qn_selected=request.POST.getlist('qn_existing')
            for i in qn_selected:
                qn=Question.objects.get(pk=i)
                q=Question.objects.create(question=qn.question, event=event)
            added=True
            question_list=Question.objects.filter(event=event)
            all_questions=Question.objects.all()
            all_questions=question_clean(all_questions,question_list)
            return render_to_response('events.html', locals(),context_instance=RequestContext(request))

    if questionid is not None:
        edit=True
        question=Question.objects.get(pk=questionid)  
        return render_to_response('events.html',locals(),context_instance=RequestContext(request)) 
             
    return render_to_response('events.html',locals(),context_instance=RequestContext(request))
    
#@Cores_only        
def viewapplication(request, user_id, event_id=None):
    choice1=Choice.objects.get(user=user, pref_no=1)
    choice2=Choice.objects.get(user=user, pref_no=2)
    choice3=Choice.objects.get(user=user, pref_no=3)
        
    if event_id is not None:
        event=Event.objects.get(pk=event_id)
        questions=Question.objects.filter(event=event)
        u=User.objects.get(pk=user_id)
        user=UserProfile.objects.get(user=u)
        answers=[]
        for q in questions.all():
            a=Answer.objects.get(user=user, question=q)
            html="<b>%s</b><br/>%s<br/>" % (str(q.question), str(a.answer))
            answers.append(html)
    return render_to_response('view_application.html',locals(),context_instance= RequestContext(request))

#@Cores_Only    
def viewapplicants(request,event_id):
    accept=reject=False
    event=Event.objects.get(pk=event_id)
    if request.method == 'POST':  
        if 'prefchoice' in request.POST:      
            pref_no = request.POST['preference']
            event=Event.objects.get(pk=event_id)
            choice=Choice.objects.filter(pref_no=pref_no,event=event, is_accepted=0)
        if 'accept' in request.POST:
            accepted=request.POST.getlist('acc_rej')
            for i in accepted:
                u=User.objects.get(pk=i)
                user=UserProfile.objects.get(user=u)
                c=Choice.objects.get(user=user)
                c.is_accepted=1
                c.save()
            accept=True
        if 'reject' in request.POST:
            rejected=request.POST.getlist('acc_rej')
            for i in rejected:
                u=User.objects.get(pk=i)
                user=UserProfile.objects.get(user=u)
                c=Choice.objects.get(user=user)
                c.is_accepted=-1
                c.save()
            reject=True
    return render_to_response("pref_choice.html",locals(),context_instance= RequestContext(request))    

#@Cores_Only
def final_list(request,event_id=None):
    if event_id is not None:
        event=Event.objects.get(pk=event_id)
        accepted=Choice.objects.filter(event=event, is_accepted=1)
        
    return render_to_response("final.html",locals()) 

    
"""
#@Coords_Only    
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
"""

