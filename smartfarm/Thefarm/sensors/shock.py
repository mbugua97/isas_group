import RPI.GPIO as GPIO # imports the GPIO modules for tho pins
import time # for working with time 


GPIO.setmode(BCM.GPIO) # To eneble use of BCM pin numbering system

shockPin = 4 # set the GPIO pin for shock

GPIO.setup(shockPin, GPIO.IN, pud=GPIO.PUD_UP) #set the pin as an input, and set it such that if it is pulled up(the sensor) it in trigaerd

while True:
    GPIO.wait_for_edge(shockPin, GPIO.FALLING) # detects when sensor is triggered

    print("Triggered!!")

    time.sleep(0.1)
    