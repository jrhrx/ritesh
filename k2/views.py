from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')