from django.shortcuts import render

# Create your views here.

def UserHomePage(request):
    return render(request, "user_app/userhome.html")
