from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello world")
    # return render("<h2>Hello World</h2>")
    return render(request= 'home.html', {'name': 'Kal'})