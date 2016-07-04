import RPi.GPIO as GPIO
import time

GPIO.cleanup()

in1 = 18
in2 = 23
in3 = 24
in4 = 25

in5 = 12
in6 = 16
in7 = 20
in8 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)




GPIO.output(in1,True)
GPIO.output(in2,False)
GPIO.output(in3,False)
GPIO.output(in4,True)

GPIO.output(in5,False)
GPIO.output(in6,True)
GPIO.output(in7,True)
GPIO.output(in8,False)

time.sleep(3)

GPIO.cleanup()
