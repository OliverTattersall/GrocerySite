from django.shortcuts import render
from .forms import CustomUserCreationForm 
from django.http import JsonResponse , HttpResponseRedirect
from .models import User, GroceryList, GroceryItem
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
        # values = list(GroceryList.objects.filter())

        values = list(map(lambda x: {'name':x.name, 'id':x.id}, values))
    print(values)

    return render(request, 'grocery_lists.html', {'grocery_lists':values})
    # return JsonResponse(values, safe=False)

def check_user_on_list(request, id):
    grocery_lists = list(request.user.grocery_list.all())
    grocery_lists = list(map(lambda x: x.id, grocery_lists))
    
    if id not in grocery_lists:
        return False
        # return HttpResponseRedirect('/g_lists')
    return True


def grocery_list(request, id):
    id = int(id)
    values = []
    if request.user.is_authenticated:
        print(id, request.user.id)
        
        if not check_user_on_list(request, id):
            return HttpResponseRedirect('/g_lists')

        # print(grocery_lists)
        values = list(GroceryItem.objects.filter(list_id = id))
        values = list(map(str, values))
        # return JsonResponse

        print(values)
    else:
        return HttpResponseRedirect('/login')

    return JsonResponse(values, safe=False)


def add_item(request, list_id):
    list_id = int(list_id)

    if request.user.is_authenticated:
        if not check_user_on_list:
            print('bad')

        queries = request.GET
        if 'food' not in queries:
            return JsonResponse({'error':'no food listed'}, safe=False)
        
        food = queries['food']
        new_food = GroceryItem(food=food, list_id=list_id)
        new_food.save()

    else:
        return HttpResponseRedirect('/login')
        


def users(request):
    # print(User.objects.values())
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
    else:
        return HttpResponseRedirect('/login')

    # print(username, request.user)

    return JsonResponse({'name':username}, safe=False)