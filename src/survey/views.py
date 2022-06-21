from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.
def home_view(request):
    print("User on website")
    if request.method == "GET":
        return render(request, 'home.html', {'range': range(10)})
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        print(request.POST)
        print(first_name, last_name)
        print(age)
        return render(request, 'home.html', {"success": True})
