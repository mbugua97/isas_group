from django.shortcuts import render


#this is the login page view

def loginpage(request):
    return render(request,'Thefarm/login.html')



#this is the homepage
def homepage(request):
    return render(request,'Thefarm/mainpage.html')



#this is the fogot password page
def fogotpssd(request):
    return render(request,'Thefarm/fpassd.html')





#this is the new user page
def newuser(request):
    return render(request,'Thefarm/newuser.html')


