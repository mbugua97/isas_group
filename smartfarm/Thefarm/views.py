from django.shortcuts import render
import cv2
import threading
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .fan import switching_fun
from .lights import switching_bulb
from .pump import switching_pump

s_Fun=switching_fun()
s_bulb=switching_bulb()
s_pump=switching_pump()



#switching the fun
@csrf_exempt
def Switch_fan(request):
    switchfan = s_Fun.read_switch()
    if switchfan == 0:
        s_Fun.set_led(False)
    else:
        s_Fun.set_led(True)

    success = True  # or False, depending on whether the script executed successfully or not

    return JsonResponse({'success': success})





#switching the bulb
@csrf_exempt
def Switch_bulb(request):
    switchbulb = s_bulb.read_switch()
    if switchbulb == 0:
        s_Fun.set_led(False)
    else:
        s_Fun.set_led(True)
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success':success})




#switching the pump
@csrf_exempt
def Switch_pump(request):
    switch = s_pump.read_switch()
    if switch == 0:
        s_Fun.set_led(False)
    else:
        s_Fun.set_led(True)
     
    success = True  # or False, depending on whether the script executed successfully or not

    return JsonResponse({'success': success})







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




