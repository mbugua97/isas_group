from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from .fan import switching_fun
from .lights import switching_bulb
from .pump import switching_pump

s_Fun=switching_fun()
s_pump=switching_pump()
s_bulb=switching_bulb()

#switching the fun  ON
@csrf_exempt
def Switch_fan_on(request):
    s_Fun.set_led(True)
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success': success})
#switching the fun off
@csrf_exempt
def Switch_fan_off(request):
    s_Fun.set_led(False)
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success': success})






#switching the bulb on
@csrf_exempt
def Switch_bulb_on(request):
    s_bulb.set_led(True)
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success':success})
#switching the bulb off
@csrf_exempt
def Switch_bulb_off(request):
    s_bulb.set_led(False)
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success':success})




#switching the pump on
@csrf_exempt
def Switch_pump_on(request):
    s_pump.set_led(True) 
    success = True  # or False, depending on whether the script executed successfully or not
    return JsonResponse({'success': success})

#switching the pump off
@csrf_exempt
def Switch_pump_off(request):
    s_pump.set_led(False) 
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




