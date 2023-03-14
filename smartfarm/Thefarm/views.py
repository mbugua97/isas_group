from django.shortcuts import render
import cv2
import threading
from django.http import StreamingHttpResponse




#this is the login page view

def loginpage(request):
    return render(request,'Thefarm/login.html')



#this is the homepage
def homepage(request):
    context = {'video_url': '/video_feed/'}
    
    return render(request,'Thefarm/mainpage.html',context)



#this is the fogot password page
def fogotpssd(request):
    return render(request,'Thefarm/fpassd.html')





#this is the new user page
def newuser(request):
    return render(request,'Thefarm/newuser.html')



def lotp(request):
    return render(request,'Thefarm/lotp.html')







