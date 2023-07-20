#main id/pass=admin
#user id=js123 , pass=js
from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
from home.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    #return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'about.html')

def counter(request):
    return render(request, 'counter.html')

# def nutrition(request):
#     return render(request, 'nutrition.html')
def nutrition(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'FPDMNGdPapIeSUTFWVSzzg==I4vkaTSa2AH5UVIy'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'nutrition.html', {'api': api})
    else:
        return render(request, 'nutrition.html', {'query': 'Enter a valid query'})



   
#Id/pass=fitness
def contact(request):
   # messages.success(request, 'Welcome to Contact')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "please fill the message Correctly !!!")
        else:
            contact=Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request, "Your messages has been Successfully Send.")

    return render(request, 'contact.html')

def test(request):
    return render(request, 'test.html')

    
def plans(request):
    return render(request, 'plans.html')

def diet(request):
    return render(request, 'diet.html')
  
  
def Signup(request):
   # messages.success(request, 'Welcome to Contact')
    if request.method=='POST':
         email=request.POST['email']
    return render(request, 'contact.html')

def muscleinfo(request):
    return render(request, 'muscle_info.html')
    

def getplans(request):
    return render(request, 'get_plans.html')


def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Fail to Logged In.")
            return redirect('home')

    return HttpResponse('404 -Not Found')
    
def handleLogout(request):  
    logout(request)
    messages.success(request, "successfully Logged out.")
    return redirect('home')



def handleSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myUser=User.objects.create_user(username, email, pass1)
        myUser.first_name=fname
        myUser.last_name=lname
        myUser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('/')
    else:
        return HttpResponse('404 -Not Found')
    
   
    

    