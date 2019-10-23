from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Message
from django.utils import timezone
from authentication.forms import Authentication_Form

response = {} 
response['message_form'] = Message_Form
response['Authentication_Form'] = Authentication_Form

def index(request):
    return render(request, 'index.html', response)

def about(request):
    return render(request, 'about.html', response)

def portofolio(request):
    return render(request, 'portofolio.html', response)

# Act Model
def guest_form(request):
    return render(request, 'form.html', response)

def message_post(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        response['email'] = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        response['message'] = request.POST['message']
        response['created_date'] = timezone.localtime()
        message = Message(name=response['name'], email=response['email'], message=response['message'], created_date=response['created_date'])
        message.save()
        return render(request,'form_result.html', response)
    else:        
        return HttpResponseRedirect('/')

def message_table(request):
    cookies_values=request.COOKIES.get('username')
    if cookies_values is None:
        return HttpResponseRedirect('authentication')
    else :
        message = Message.objects.all().values()
        response['message'] = message
        html = 'table.html'
        return render(request, html , response)
