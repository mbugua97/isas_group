import RPi.GPIO as GPIO
import time
 
# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.IN)
 
# Function to read soil moisture level
def read_soil_moisture():
    # Turn on the sensor
    GPIO.output(14,GPIO.HIGH)
    time.sleep(0.1)
    # Read analog value from sensor
    soil_moisture = GPIO.input(15)
    # Turn off the sensor
    GPIO.output(14,GPIO.LOW)
    return soil_moisture
 
# Read soil moisture level every 10 seconds
while True:
    soil_moisture = read_soil_moisture()
    print("Soil Moisture: ", soil_moisture)
    time.sleep(10)
