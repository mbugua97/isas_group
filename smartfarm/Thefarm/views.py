from django.shortcuts import render


#this is the login page view

def loginpage(request):
    return render(request,'Thefarm/login.html')



#this is the homepage view
def homepage(request):
    return render(request,'Thefarm/mainpage.html')