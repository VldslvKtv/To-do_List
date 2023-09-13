from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RecordForm
from .models import Record, EXECUTION_STATUS


# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todo')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'This login has already in use.'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                            'error': 'Password did not match.'})


def current_todo(request):
    records = Record.objects.filter(user=request.user, status=EXECUTION_STATUS[1][0])  # user=request.user
    return render(request, 'todo/current_todo.html', {'records': records})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('current_todo')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': RecordForm()})
    else:
        try:
            form = RecordForm(request.POST)
            new_record = form.save(commit=False)
            new_record.user = request.user
            new_record.save()
            return redirect('current_todo')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': RecordForm(),
                                                            'error': 'Incorrect data transmitted'})


def viewrecord(request, record_pk):
    record = get_object_or_404(Record, pk=record_pk, user=request.user)
    if request.method == 'GET':
        form = RecordForm(instance=record)
        return render(request, 'todo/viewrecord.html', {'record': record, 'form': form})
    else:
        try:
            form = RecordForm(request.POST, instance=record)
            form.save()
            return redirect('current_todo')
        except ValueError:
            return render(request, 'todo/viewrecord.html', {'form': RecordForm(),
                                                            'error': 'Incorrect data transmitted'})


def deleterecord(request, record_pk):
    if request.method == 'POST':
        record = get_object_or_404(Record, pk=record_pk, user=request.user)
        record.delete()
        return redirect('current_todo')


def home(request):
    return render(request, 'todo/home.html')
