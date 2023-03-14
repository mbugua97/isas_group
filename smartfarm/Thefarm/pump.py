import RPi.GPIO as GPIO

LED_PIN = 25
SWITCH_PIN = 8

class switching_pump(object):
  """Raspberry Pi Internet 'Thing'. """
  
  def __init__(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)    #LED as an output
    GPIO.setup(SWITCH_PIN, GPIO.IN)     #Switch as an input
       
  def read_switch(self):
   """Read the state of the switch and return it (as a boolean).
   """
   return GPIO.input(SWITCH_PIN)

  def set_led(self, value):
   """Change the LED to the passed in valaue, either True for on or False for off. """
   GPIO.output(LED_PIN, value)

