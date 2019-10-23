from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import Authentication_Form
from django.contrib.auth import authenticate, login, logout
from homepage.forms import Message_Form

response = {} 
response['Authentication_Form'] = Authentication_Form
response['message_form'] = Message_Form
def login_forms(request):
    cookies_values=request.COOKIES.get('username')
    if cookies_values is None:
        return render(request, 'registration/login.html', response)
    else :
        return render(request, 'index.html', response)

def authentication(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response_action = HttpResponseRedirect('/')
                response_action.set_cookie('username', username)
                return response_action
    return HttpResponseRedirect('authentication')

def logout_account(request):
    logout(request)
    action_logout = HttpResponseRedirect('/')
    action_logout.delete_cookie('username')
    return action_logout