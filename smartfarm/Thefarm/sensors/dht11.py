import Adafruit_DHT  #gets the module for working with the  DHT sensor series for humidity and temperature 
import time # time module that is used when working with time related applications

DHT_SENSOR = Adafruit_DHT.DHT11 # initialises the variable  DHT_SENSOR to specifically hold values from the DHT11 sensor from the Adafruit_DHT module
DHT_PIN = 4 # initiates DHT_PIN to pin 4 of the raspberry pi

while True: # while loop creates an infinite loop used to run the code for reading values repeatedly
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) # takes the values from the DHT sensor and stores them in the variables humidity and temperature
    if humidity is not None and temperature is not None: # checks if there values stored in the variables humidity and temperature
        print("temp = {0:0.1f}C humu{1:0.1f}%".format(temperature, humidity)) # if values are present they are printed on the console
    else:
        print("sensor failure. check wiring.") # if the values are not there then a error message is printed on the console
    time.sleep(3) # time.sleep(3) is a funtion used to delay the program from running for 3 second