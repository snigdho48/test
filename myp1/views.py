from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def index  (request):
 return render(request,'project1/index.html')

def Blog(request):
 return render(request,'project1/Blog.html')

def Help(request):
 return render(request,'project1/Help.html')

def Shop(request):
 return render(request,'project1/Shop.html')

def Signin(request):
 return render(request,'project1/Signin.html')

def Signup(request):
 return render(request,'project1/Signup.html')

def Track(request):
 return render(request,'project1/Track-your-order.html')

def essential(request):
 return render(request,'project1/essential.html')

def cont1(request):
    return redirect("https://www.bigcommerce.com/blog/holiday-gift-guide/")
