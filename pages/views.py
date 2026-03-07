from django.shortcuts import render, redirect
from .models import Login
# from django.http import HttpResponse

# Create your views here.

def index(request):
    x = {'name':'mostafa ali taha',
         'age':255}
    return render(request, 'pages/index.html', x)
    # return HttpResponse('index page')


def about(request):
     return render(request, 'pages/about.html')
    # return HttpResponse('About page')
    
def login(request):    
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          email = request.POST.get('email')
          if username and password and email:    #معناها طلما موجود بيانات فعليا 
               data = Login(username = username, password = password, email=email)
               data.save()
               return redirect('login')
     # # print(username)
     # # print(password)
     return render(request, 'pages/login.html')
    # return HttpResponse('About page')