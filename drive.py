import RPi.GPIO as GPIO
import time
import car

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

car = car.Car([24,25,18,23,12,16,20,21],GPIO.LOW)

car.lunch()

car.forward()
time.sleep(10)

car.stop()
car.terminate()

GPIO.cleanup()
