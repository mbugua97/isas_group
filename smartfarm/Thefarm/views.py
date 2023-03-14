from django.shortcuts import render
import cv2
import threading
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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


#this is the otp login
def lotp(request):
    return render(request,'Thefarm/lotp.html')




#switching the bulb
@csrf_exempt
def Switch_bulb(request):
    success = True  # or False, depending on whether the script executed successfully or not

    return JsonResponse({'success': success})


#switching the fun
@csrf_exempt
def Switch_fan(request):
    success = True  # or False, depending on whether the script executed successfully or not

    return JsonResponse({'success': success})

#switching the pump
@csrf_exempt
def Switch_pump(request):
    success = True  # or False, depending on whether the script executed successfully or not

    return JsonResponse({'success': success})

