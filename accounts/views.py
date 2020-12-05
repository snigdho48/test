from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate




# Create your views here.



def Signup(request):

    if request.method == 'POST':
        first_name= request.POST['First_Name']
        last_name= request.POST['Last_Name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken.')

                return redirect('Signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken.')

                return redirect('Signup')

            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'Account created successfully.')
                return redirect('Signup')

        else:
            messages.info(request,"Password didn't match.")
            return redirect('Signup')

    else:
            return render(request,'project1/Signup.html')


def Signin(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('username')
        password= request.POST.get('password')
        User._meta.get_field('email')._unique = True



        if User.objects.filter(username=username).exists():
            user= auth.authenticate(username=username,password=password)



        elif User.objects.filter(email=email).exists():
            username = User.objects.get(email=email.lower()).username
            user= authenticate(username=username,password=password)



        else:
            messages.info(request,'Enter valid username or email')
            return redirect('Signin')





        if user is not None:

            auth.login(request,user)
            messages.info(request,'Signin successfully.')
            return redirect('/')

        else:
            messages.info(request,'incorrect password.')
            return redirect('Signin')



    else:
        return render(request,'project1/Signin.html')






def logout(request):

    auth.logout(request)
    return redirect('/')
