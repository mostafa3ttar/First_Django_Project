from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    x = {'name':'mostafa ali taha',
         'age':255}
    return render(request, 'pages/index.html', x)
    # return HttpResponse('index page')


def about(request):
    y = {'name':'mostafa ali taha',
         'age':255}
    return render(request, 'pages/about.html', y)
    # return HttpResponse('About page')