from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def home_view(request):
    print("User on website")
    return render(request, 'home.html')
