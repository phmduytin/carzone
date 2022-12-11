from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Contact
from cars.models import car
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are logging!!!')
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now loggin success!!!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password not correct!!!')
            return redirect('login')
   

    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return redirect('home')

def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is exists!!!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is exists!!!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now loggin success!')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are register success!')
                    return redirect('login')
        else:
            messages.error(request, 'Password is not match!!!')
            return redirect('register')

    
   
    return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    user_filter = Contact.objects.filter(user_id = request.user.id).order_by('-created_date')
    
    check = '0'
    cars_filter = []

    for i in user_filter:
        car_single = car.objects.get(pk=i.car_id)
        cars_filter.append(car_single)

    context = {
        'cars_filter': cars_filter,
    }


    return render(request, 'accounts/dashboard.html', context)