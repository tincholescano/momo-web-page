from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .models import Document
from .forms import DocumentForm
from .forms import SignUpForm

def index(request): 
    return render(request, 'home.html')

def profile(request): 
    return render(request, 'perfil.html')

def loginv(request):
    if request.method != "POST":
        return redirect('index')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
    return redirect('index')

def logoutv(request):
    logout(request)
    return redirect('index')

def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'home.html', {
        'form': form
    })

def display_document(request, document_id):
    image = Document.objects.get(pk=document_id)
    return render(request, 'display_document.html', {'image': image})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'home.html', {'form': form})
