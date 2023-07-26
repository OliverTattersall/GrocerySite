from django.shortcuts import render
from .forms import CustomUserCreationForm 
from django.http import JsonResponse , HttpResponseRedirect
from .models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
# Create your views here.  
  
def register(request):  
    print(request)
    form  = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        print('hello')
        form.save()
    # if request.POST:  
    #     print('hello')
    #     form = CustomUserCreationForm()  
    #     if form.is_valid():  
    #         form.save()  
    # else:  
    #     form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context) 
# Create your views here.

def lists(request):
    values = []
    if request.user.is_authenticated:
        print('hello')
        values = list(request.user.grocery_list.all())

    
    values = list(map(lambda x: x.objects.values(), values))
    print(values)

    return JsonResponse(list(values), safe=False)



def users(request):
    return JsonResponse(list(User.objects.values()), safe=False)


def login_page(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            raise ValidationError("The username or password was wrong")

    return render(request, 'login.html', {'form':form})

def index(request):

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    print(username)

    return JsonResponse({'name':username}, safe=False)