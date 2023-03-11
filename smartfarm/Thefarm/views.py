from django.shortcuts import render

def loginpage(request):
    return render(request,'Thefarm/login.html')