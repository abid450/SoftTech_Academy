from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import SoftTech_Student_id
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import *
import uuid
from .utils import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def login(request):
    return render(request,'login.html')


# Register form ------------------------------------
@csrf_exempt
def register(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirmpassw = request.POST.get('password2')
        user_obj = User(username = email)
        user_obj.set_password (password)
        p_obj = SoftTech_Student_id.objects.create(
            user = user_obj,
            email_token = str(uuid.uuid4())
        )
        send_email_token(email,p_obj.email_token)

        if password!=confirmpassw:
            messages.warning(request, 'Password did not Match !') 
            return redirect('/register_c')
       

        try:
            if User.objects.get(username=usern):
                messages.error(request,'This Username Already Exist')
                return redirect('/register_c')
            
        except:
            pass
        
        try:
            if User.objects.get(email=email):
                messages.error(request, 'This Email Already Exist')
                return redirect('/register_c')
        except:
            pass

    
        user = User.objects.create_user(usern,email,password,confirmpassw)
        user.save()    
        messages.success(request, 'You are Successfully Sign Up')
        return redirect('/register_c')
    return render(request, 'register.html')



def verify(request, token):
    try:
        obj = SoftTech_Student_id.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        messages.success(request, 'your account verify')
    
    except Exception as e:
        messages.success(request, 'invalid token')

# Alert Form -------------------------------------------------
def alert_message(request):
    
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        age = request.POST['age']
        biography = request.POST['biography']
        course_name = request.POST['course_name']
        interest = request.POST['interest']

        
      

        if SoftTech_Student_id.objects.filter(email=email).exists() or SoftTech_Student_id.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'This Value Already Exist, Please Try Another Value')

        

        else:
            contect = SoftTech_Student_id(name=name,email=email,phone_number=phone_number,age=age,biography=biography,course_name=course_name,interest=interest)
            contect.save()
            #messages.success(request, 'Congratulations🎉🎉🎉 আপনি আমাদের কোর্সে সফল ভাবে এনরোল করেছেন')
            return HttpResponseRedirect('/message_re')
        
    return render(request, 'alert.html')

# Alert Form Redirect -------------------------------------
def message_re(request):
    #messages.success(request,'You are Successfully Enroll Now')
    return render(request, 'redirect.html')