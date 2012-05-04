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
    Home Page of Application Portal. Also has login. 
    
    """
    if(request.method=='POST'):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            temp = UserProfile.objects.get(UserProfile.user=request.user)
            if temp.is_core==False:
                return render_to_response("coord_home.html",locals(),context_instance=RequestContext(request))
            else:
                return render_to_response("core_home.html",locals(),context_instance=RequestContext(request))   
    	else:
    	#Must create Invalid message display
		return render_to_response("Home.html",locals(),context_instance=RequestContext(request))
    return render_to_response("Home.html",locals(),context_instance=RequestContext(request))

    
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
def core_question_add_existing(request,idofevent)
    all_questions=Question.objects.all()
    return render_to_response('viewquestion.html',locals(),context_instance=RequestContext(request))
    
