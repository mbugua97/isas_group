from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from twilio.rest import Client


#twilio
otp=random.randint(1111,9999)
auth_token="900062764324071aa543c688b0d2ea4c"
auth_id="AC9ae150dd36651e026e92d90da90a935f"

client=Client(auth_id,auth_token)









#from .fan import switching_fun
#from .lights import switching_bulb
#from .pump import switching_pump

#s_Fun=switching_fun()
#s_pump=switching_pump()
#s_bulb=switching_bulb()

#switching the fun  ON
#@csrf_exempt
#def Switch_fan_on(request):
 #   s_Fun.set_led(True)
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success': success})
#switching the fun off
#@csrf_exempt
#def Switch_fan_off(request):
 #   s_Fun.set_led(False)
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success': success})






#switching the bulb on
#@csrf_exempt
#def Switch_bulb_on(request):
 #   s_bulb.set_led(True)
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success':success})
#switching the bulb off
#@csrf_exempt
#def Switch_bulb_off(request):
 #   s_bulb.set_led(False)
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success':success})




#switching the pump on
#@csrf_exempt
#def Switch_pump_on(request):
 #   s_pump.set_led(True) 
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success': success})

#switching the pump off
#@csrf_exempt
#def Switch_pump_off(request):
 #   s_pump.set_led(False) 
  #  success = True  # or False, depending on whether the script executed successfully or not
   # return JsonResponse({'success': success})







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
    if request.method=='POST':
        phone=request.POST.get("phone")
        print(phone)
    return render(request,'Thefarm/lotp.html')




def gotp(request):
    
    return render(request,'Thefarm/gotp.html')