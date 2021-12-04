# Los módulos necesarios serán importados y configurados

import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# El pin de entrada que está conectado con el sensor

GPIO_PIN = 21
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
  
print "KY-010 Sensor Test [press ctrl+c to end the test]"
  
def outputFunction(null):
        print("Sensor is blocked")
  
# detección de señal (flanco ascendente).

GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=outputFunction, bouncetime=100) 
  
# Trabajo de recolección de residuos una vez finalizado el programa

try:
        while True:
                time.sleep(1)
  
# Scavenging work after the end of the program

except KeyboardInterrupt:
        GPIO.cleanup()

