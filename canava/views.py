from django.shortcuts import render,HttpResponseRedirect
from .models import alert_message_m

from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request, 'register.html')





def alert_message(request):
    
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        age = request.POST['age']
        biography = request.POST['biography']
        job_role = request.POST['job_role']
        interest = request.POST['interest']

        
        if len(email)<22:
            messages.warning(request,'Invalid This email, Please Enter Your Correct Email')

        if alert_message_m.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'This Number Already Exist, Please Enter Your Correct Number')
        
        if alert_message_m.objects.filter(email=email).exists():
            messages.error(request,'This Email Account Already Exist, Please Enter a Another Account')

        else:
            contect = alert_message_m(name=name,email=email,phone_number=phone_number,age=age,biography=biography,job_role=job_role,interest=interest)
            contect.save()
            
            return HttpResponseRedirect('/message_re')
        
    return render(request, 'alert.html')

def message_re(request):
    messages.success(request,'Your message has been Successfully Sent')
    return render(request, 'redirect.html')