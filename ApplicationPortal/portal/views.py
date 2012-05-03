from django.contrib.auth.models import Group

# Create your views here.

def super_home(request):
    """
    To display super user's home page.  This page will have tables of core details and groups.
    The super user can add/edit a group and its permissions
 
    """
    group=Group.objects.all()
    #Add core object here
    return render_to_response('/super_home/',locals(),context_instance= RequestContext(request))
    
    	
