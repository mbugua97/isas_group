import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

# Code to activate the relay will go here
GPIO.output(14,GPIO.HIGH)


GPIO.output(14,GPIO.LOW)

# Clean up GPIO
GPIO.cleanup()
