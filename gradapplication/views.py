from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from gradapplication.models import Farm,PublicPlace,FarmBooking,User
from django.db.models import Subquery
# from django.contrib.auth.models import User


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm

def create_account(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form data to create a new user object
            # Perform any additional actions, such as sending a confirmation email
            return redirect('create')  # Replace 'login' with the URL name of your login page
    else:
        form = CreateUserForm()
    return render(request, 'create_account.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the URL name of your home page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def farms(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})    # myfarms = User.objects.all().values() #البيانات الجاية من db
    # template = loader.get_template('index.html')
    # context = {
    # 'myfarms': myfarms, #dictionary #البيانات بحد ذاتها
    # }
    # return HttpResponse(template.render(context, request)) 



# def farms(request):
#     # myfarms = User.objects.filter(isOwner=True) #البيانات الجاية من db
#     # myfarms = User.objects.filter(userName__startswith="l") #البيانات الجاية من db
#     template = loader.get_template('index.html')
#     context = {
#     'myfarms': myfarms, #dictionary #البيانات بحد ذاتها
#     }
#     return HttpResponse(template.render(context, request)) 


# def farms(request):
#     data = FarmBooking.objects.select_related('farmbooking__farmId').values('userId', 'farmbooking__farmId__name' )
#     # Pass the data to the template or do further processing
#     return render(request, 'index.html', {'data': data})