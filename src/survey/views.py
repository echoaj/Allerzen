from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.
def home_view(request):
    print("User on website")
    return JsonResponse({"message": "hi"})
