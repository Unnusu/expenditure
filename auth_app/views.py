from django.shortcuts import redirect, render
from auth_app.forms import PersonForm, PersonLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=='GET':
        form = PersonForm()
        return render(request,'register.html',{'form':form})
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            mail = form.cleaned_data['email']
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            
            User.objects.create_user(first_name=fname,last_name=lname,email=mail,username=uname,password=pword)
            

            subject = 'Account Creation'
            message = f'Hi {fname} {lname} thank you for registering . Your username is {uname}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail,'unnayanthapa77@gmail.com']
            
            send_mail( subject, message, email_from, recipient_list,fail_silently=False)
            
            
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})
        

def signin(request):
    if request.method == 'GET':
        form = PersonLoginForm()
        return render(request,'login.html',{'form' : form})
    else:
        username= request.POST['username']
        password= request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:         
            login(request,user)
            next = request.GET.get('next')
            if next is None:
                return redirect('home')
            else:
                return redirect(next)
        else:
            form = PersonLoginForm
            messages.error(request,'Invalid Username or Password')
            return render(request,'login.html',{'form' : form})
        
def signout(request):
    logout(request)
    return redirect('login')
    