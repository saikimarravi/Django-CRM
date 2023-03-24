from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged In !")
            return redirect ('home')
        else:
            messages.success(request,"There Was An Error Logging in ! Please Try Again...... ")
            return redirect ('home')
    else:
        return render(request,'crm/index.html',{})    
    
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out.....!")
    return redirect ('home')
def register_user(request):
    return render(request ,'crm/register.html',{})
    
