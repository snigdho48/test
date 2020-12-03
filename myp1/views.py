from django.shortcuts import render

from .models import new1
from django.shortcuts import redirect

# Create your views here.

def index(request):
    mys = new1.objects.all()

    return render(request, 'project1/index.html', {'mys': mys})



def Blog(request):
    return render(request, 'project1/Blog.html')

def Help(request):
 return render(request,'project1/Help.html')

def Shop(request):
 return render(request,'project1/Shop.html')



def Track(request):
 return render(request,'project1/Track-your-order.html')

def essential(request):
 return render(request,'project1/essential.html')

def cont1(request):
    return redirect("https://www.bigcommerce.com/blog/holiday-gift-guide/")
