from django.shortcuts import render , redirect
from contest.forms import RegistrationForm ,LoginForm
from question.models import Profile
from contest.functions import contest_phase
from django.contrib.auth import logout , authenticate,login



def home(request):
    data = {}
    template = 'contest/home.html'
    return render(request, template, data)


def register(request):
    context = {}
    template = 'contest/register.html'
    if contest_phase() != 'after':
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                uname = form['username'].value()
                pwd = form['password'].value()
                p = Profile()
                p.username = uname
                p.set_password(pwd)
                p.save()
                context['successful_registration'] = uname
                return redirect('home')
            else:
                form = RegistrationForm()

    return render(request, template, {'form':form})


def unauthorized(request):
    return render(request, 'unauthorized.html')


def logout_user(request):
    logout(request)
    return render(request,'logged_out.html')


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':

        form = LoginForm(request.POST)
        uname = form['username'].value()
        pwd = form['password'].value()
        user =  authenticate(username =uname,password=pwd)
        if user is not None:
            login(request,user)
        else:
            return redirect("home")


        return redirect('home')
    else:
        form = LoginForm()

    

    return render(request,'login.html',{'form':form})