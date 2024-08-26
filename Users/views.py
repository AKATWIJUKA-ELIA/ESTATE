from django.shortcuts import render,redirect
from Users.models import auth
from django.core.mail import send_mail
from email.message import EmailMessage
import ssl
import smtplib
from django.core import serializers
import string
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def send_email(request):
      password = 'hhyx mfca zpvo ckof'
      recepient_list=[]
      if request.method == "POST":
            
            email = request.POST['pwd_email']
            print(email)
            if User.objects.filter(email=email).exists():
                  recepient_list.append(email)
                  send_mail("PASSWORD RESET", f"Your password reset key is {random_no} \n Do not share this key with anyone",from_email="eliaakjtrnq@gmail.com",recipient_list=recepient_list,fail_silently=False,auth_password= password)
                  recepient_list.clear()
           
            elif User.objects.filter(email=email).none():
                  messages.warning(request,'Email does not exist! Please register first to get access.')
                  return redirect('forgot_password')
            
            else:
                  pass


def change_password():
      pass

def forgot_password(request):
      return render(request, "registration/forgotpassword.html")
      
      # return HttpResponse("Please enter your username or e-mail address to recover your password.\n\nYou will receive a link to create a new password via e-mail if you provide correct")


def signup(request):
      if request.method == "POST":
            #first_name = request.POST.get('first_name')
            #print(first_name)
            #last_name = request.POST.get('last_name')
            username = request.POST.get('username').lower()
            email = request.POST['email']
            #phone = request.POST['phone']
            password = request.POST['password']
            password2 = request.POST['password2']
            
            if password == password2:
                  
                  if User.objects.filter(username = username).exists():
                        messages.error(request,"Username already exists.")
                        return render(request, 'registration/signup.html')
                  
                  elif User.objects.filter(email = email).exists():
                        messages.error(request,"email already exists.")
                        return render(request, 'registration/signup.html')   
                  else:
                        NewUser = User.objects.create_user(username,email,password)
                        
                        NewUser.save()
                        messages.success(request, "Your account has been successfully created you will be redirected to the login page")
                        return redirect('home') 
            
            else:
                  messages.error(request,"Passwords do not match.")
                  return render(request, 'registration/signup.html')
      
      
      return render(request, 'registration/signup.html')


def home(request):
      if request.method == "POST":
            username = request.POST.get('username')#.lower()
            password = request.POST.get('password')
            current_user_email = User.objects.get(username=username)
            current_user_email1 = current_user_email.email
            email_list.append(current_user_email1)
            username_list = username.capitalize()     
            print(username_list)
            #email = current_user_email1
            
            print(current_user_email1)
            
            user = authenticate(username = username, password=password)
            
            if user:                        
                  login(request,user)
                  username=user.username
                  #self.logged_in = True
                  return render(request,'registration/dashboard.html', {'username': username.capitalize()})
                  
            else:
                  messages.error(request, "bad credentials")
                  return redirect('booking')
            #retrieving data
      data = serializers.serialize("python",booking_information.objects.all() )
      context = {'data':data,}    
                  
      return render(request, "registration/index.html", context)
email_list = []
username_list = []

