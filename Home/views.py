from django.shortcuts import render

# Create your views here.

def home(request):
    print(request.user)
    return render(request, 'home.html')
