'''
Put @Coords_Only before all views that are for Coords.
Put @Cores_Only before all views that are for Cores.
Put @login_required if the page has no permissions.

Include <from django.contrib.auth.decorators import login_required> for @login_required
Include this file for @Coords_only and @Cores_Only
'''

class Coords_Only(object):
    def __init__(self,views_func):
        self.views_func = views_func
        
    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            User=UserProfile.objects.get(UserProfile.username=str(request.user))
            if request.user.is_authenticated() and User.is_core==False:
                self.views_func(request, *args, **kwargs)
            else:
                HttpResponseRedirect(#No permission) 
                
        else:
            HttpResponseRedirect(#notloggedin) 

class Cores_Only(object):
    def __init__(self,views_func):
        self.views_func = views_func
        
    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            User=UserProfile.objects.get(UserProfile.username=str(request.user))
            if request.user.is_authenticated() and User.is_core==True:
                self.views_func(request, *args, **kwargs)
            else:
                HttpResponseRedirect(#No permission) 
                
        else:
            HttpResponseRedirect(#notloggedin) 


