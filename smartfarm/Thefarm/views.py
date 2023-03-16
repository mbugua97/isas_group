from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from twilio.rest import Client
from django.contrib import messages
import pickle

#importing the db
from . models import HumidityTemp,UserDetails






#twilio bob's account
otp=random.randint(1111,9999)
auth_token="390310ac28e9f5d06492a11526e0e42b"
auth_id="ACca19a7e3a5e1b132377b6898d3bb60cf"


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
    User=UserDetails.objects.all()
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('passd')
        for i in User:
            print(i.phone_number)
            if str(i.phone_number)==str(phone):
                if str(i.user_password)==str(password):
                    messages.success(request, f'hello {phone} you are logged in')
                    return redirect('hpage')
                else:
                    messages.error(request, 'check your phone number or password ')
                    return redirect('loginpage')
                    
                    
        messages.error(request, 'check your phone number or password ')
        

               



    return render(request,'Thefarm/login.html')



#this is the homepage
def homepage(request): 
    from reportlab.pdfgen import canvas
    # Create a new PDF object
    pdf = canvas.Canvas('report.pdf')

    # Add some text to the PDF
    pdf.drawString(100, 750, "Welcome to my isas")

    # Save the PDF
    pdf.save()
    return render(request,'Thefarm/mainpage.html')



#this is the fogot password page
def fogotpssd(request):
    User=UserDetails.objects.all()
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('passd')
        for i in User:
            if str(i.phone_number)==str(phone):
                person = UserDetails.objects.get(phone_number=phone)
                person.phone_number=phone
                person.user_password=password
                person.save()
                return redirect('loginpage')  

        messages.error(request, 'to reset password enter valid phone registered with')       

    return render(request,'Thefarm/fpassd.html')





#this is the new user page
def newuser(request):
    User=UserDetails()
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('passd')
        conphone=UserDetails.objects.all()
        for i in conphone:
            if i.phone_number==phone:
                messages.error(request, 'Phone is taken try a new number')
                return redirect('newuser')
        person = UserDetails(phone_number=phone, user_password=password)
        person.save()
        return redirect('loginpage')     
    return render(request,'Thefarm/newuser.html')


#this is the otp login
def lotp(request):
    if request.method=='POST':
        phone=request.POST.get("phone")
        name=request.POST.get("name")

        conphone=UserDetails.objects.all()
        for i in conphone:
            if i.phone_number==phone:
               print("match found")
               msg=client.messages.create(
                    body=f"  I.S.A.S:  hello {name} your otp is {otp}",
                    from_="+15075640261",
                    to=phone
                    )
               return redirect('gotp')
        messages.error(request, 'try a number registered with ISAS')
        return redirect('lotp')

    return render(request,'Thefarm/lotp.html')




def gotp(request):
     if request.method=='POST':
        otpno=request.POST.get("otp")
        atb=int(otp) == int(otpno)
        if atb==True:
             return redirect('hpage')
        else:
            return redirect('lotp')
     return render(request,'Thefarm/gotp.html')

#this page is for to test the model
def mlprediction(request):
    with open("Thefarm/crop_model.pkl", 'rb') as f:
        model = pickle.load(f)
    if request.method=='POST':
        Hum=request.POST.get('humidity')
        temp=request.POST.get('temprature')
        new_data = [[temp,Hum]]
        prediction = model.predict(new_data)
        context={'prediction':prediction}
        return render(request,'Thefarm/prediction.html',context)
    return render(request,'Thefarm/prediction.html')