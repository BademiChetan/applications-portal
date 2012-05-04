from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.core.context_processors import csrf
from portal.models import *
from django.shortcuts import *
from django import forms
from ../forms import *

    		
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/home/')
			
	else:
		form = RegistrationForm()
	return render_to_response('template/registration.html',{'form':form,},context_instance=RequestContext(request))



def home(request):
    """
    Home Page of Application Portal. Also has login. Part 1
    checks if user is already logged in and then redirects
    to the corresponding page. Part 2 is for logging in.
    
    """
    if request.user.is_authenticated():
        curr_user= UserProfile.objects.get(user=request.user)
        if request.user.is_superuser:
            return HttpResponseRedirect("/super_home/")
        else:    
      	    if curr_user.is_core==False:
                return HttpResponseRedirect("/coord_home/")
            else:
                return HttpResponseRedirect("/core_home/")  
		
    if(request.method=='POST'):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)


            curr_user = UserProfile.objects.get(user=request.user)
            if request.user.is_superuser:
                return HttpResponseRedirect("/super_home/")
            else:    
      	        if curr_user.is_core==False:
                    return HttpResponseRedirect("/coord_home/")
                else:
                    user=UserProfile.objects.get(user=request.user)
                    event=Event.objects.filter(group=user.group)
                    return render_to_response("core_home.html",locals(),context_instance=RequestContext(request))   
    	else:
            invalid_login=1
    return render_to_response("home.html",locals(),context_instance=RequestContext(request))


    

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
    
    """
    if request.method == 'POST':
		form = AddGroup(request.POST)
		if form.is_valid():
			new_group = form.save()
			return HttpResponseRedirect('/super_home/')
			
    else:
	    form = AddGroup()
    return render_to_response('addgroup.html',{'form':form,},context_instance=RequestContext(request))
   
    
@Coords_Only    
def coord_home(request):
    user=UserProfile.objects.get(user=request.user)
    return render_to_response("home.html",{'user':user})
    
@Cores_Only
def core_home(request):
    user=UserProfile.objects.get(user=request.user)
    return render_to_response("home.html",{'user':user})    

    
    	
def viewapplication(request,temp):
    users=UserProfile.objects.get(UserProfile.username=temp)
    choice=Choice.objects.get(Choice.user=users)
    questions=Question.objects.get(Question.event=choice.choice)
    answers=Answer.objects.get(Answer.useer=users,Answer.question=questions)
    return render_to_response('view_application.html',locals(),context_instance= RequestContext(request))


@Cores_Only    
def viewevent(request,event_id):
    if request.method == 'POST':  
        if 'prefchoice' in request.POST:  	
            pref_no = request.POST['preference']
            choice.Choice.objects.filter(pref_no=pref_no,event=event)
        if 'accept' in request.POST:
            pass#needs to be done
        if 'reject' in request.POST:
            pass#needs to be done. Accept values from checkbox
    return render_to_response("pref_choice.html",locals())

    
"""

def judgementday(request,eventid=None):
    events=Event.objects.all()
    if eventid is not None:
        event=Event.objects.get(Event.id=eventid)
        accepted=Choice.objects.filter(event.id=eventid, is_accepted=1)
        
    return render_to_response("final.html",locals())




