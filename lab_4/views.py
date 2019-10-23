from django.shortcuts import render
from homepage.forms import Message_Form

response = {} 
response['message_form'] = Message_Form
def index(request):
    return render(request, 'lab_4/lab_4.html', response)