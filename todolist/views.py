from todolist.models import toDoList
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.forms import ChoresForm, MarkedChoresForm
import datetime, json

# TODO: Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        'nama': 'Farras Hafizhudin Indra Wijaya',
        'npm' : '2106652682'
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_ascards(request):
    todolist_data = toDoList.objects.filter(user = request.user)

    context = {
        'todolist': todolist_data,
        'nama': 'Farras Hafizhudin Indra Wijaya',
        'npm' : '2106652682'
    }
    return render(request, "todolist-ascards.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_chores(request):
    if request.method == "POST":
        form = ChoresForm(request.POST)
        if form.is_valid():
            data = toDoList(
                user = request.user,
                creation_date = datetime.datetime.now(),
                title = form.cleaned_data["name"],
                description = form.cleaned_data["description"]
            )
            data.save()
            return redirect('todolist:show_todolist')
    
    form = ChoresForm()
    context = {'form':form}
    return render(request, 'addchores.html', context)

def mark_chores(request):
    if request.method == "POST":
        id = request.POST["id"]
        data = toDoList.objects.get(id=id)
        data.is_finished = not data.is_finished
        data.save()

    return HttpResponse()

def delete_chores(request):
    if request.method == "POST":
        id = request.POST["id"]
        data = toDoList.objects.get(id=id)
        data.delete()

    return redirect('todolist:show_todolist')

def show_json(request):
    data = serializers.serialize("json", toDoList.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    todolist_data = toDoList.objects.filter(user = request.user)
    response = serializers.serialize("json", todolist_data)
    return HttpResponse(response, content_type="application/json")

@login_required(login_url='/todolist/login/')
def post_todolist_ajax(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        # print("USERRRR " + request.user.id)
        instance = toDoList(user = request.user, creation_date = datetime.datetime.now(), title = title, description = description)
        instance.save()
        
        data = {
            "message": 'Submitted Successfully!'
        }
        json_object = json.dumps(data, indent = 4) 

        return JsonResponse(json.loads(json_object))
    return redirect("todolist:add_chores")