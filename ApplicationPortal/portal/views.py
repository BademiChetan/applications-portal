from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.core.context_processors import csrf
from portal.models import *
from django.shortcuts import *
from django import forms
from forms import*

    		
def register():
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

def super_home(request):
    """
    To display super user's home page.  This page will have tables of core details and groups.
    The super user can add/edit a group and its permissions
 
    """
    if(request.method=='POST'):
        try:
            request.POST['add']=="Add"
        except:
            try:
                temp=request.POST['Edit']
            except:
                temp=request.POST['Del']
                return redirect('/delgroup/'+temp)
            return redirect('editgroup/'+temp)
        return redirect('/addgroup')
    group=Group.objects.all()
    #Add core object here
    return render_to_response('super_home.html',locals(),context_instance= RequestContext(request))

#def addgroup(request, temp):
    
    
@Coords_Only    
def coord_home(request):
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    return render_to_response("home.html",{'user':user})
    
@Cores_Only
def core_home(request):
    user=UserProfile.objects.get(UserProfile.username=str(request.user))
    return render_to_response("home.html",{'user':user})    
    
    	


