import RPi.GPIO as GPIO
import time

class L298N_GPIO(object):
    '''
    This Class is for GPIO to control L298N
    '''

    __in1 = 0
    __in2 = 0
    __in3 = 0
    __in4 = 0
    __real_true = GPIO.HIGH

    def __init__(self,in1,in2,in3,in4,real_true = GPIO.HIGH):
        self.__in1 = in1
        GPIO.setup(self.__in1,GPIO.OUT)
        self.__in2 = in2
        GPIO.setup(self.__in2,GPIO.OUT)
        self.__in3 = in3
        GPIO.setup(self.__in3,GPIO.OUT)
        self.__in4 = in4
        GPIO.setup(self.__in4,GPIO.OUT)
        self.__real_true = real_true

    def forward(self):
        GPIO.output(self.__in1,self.__real_true)
        GPIO.output(self.__in2,not self.__real_true)
        GPIO.output(self.__in3,not self.__real_true)
        GPIO.output(self.__in4,self.__real_true)

    def back(self):
        GPIO.output(self.__in1,not self.__real_true)
        GPIO.output(self.__in2,self.__real_true)
        GPIO.output(self.__in3,self.__real_true)
        GPIO.output(self.__in4,not self.__real_true)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

l298n1 = L298N_GPIO(18,23,24,25,GPIO.HIGH)
l298n2 = L298N_GPIO(12,16,20,21,GPIO.LOW)


l298n1.forward()
l298n2.forward()
time.sleep(3)

l298n1.back()
l298n2.back()
time.sleep(3)

l298n1.forward()
l298n2.back()
time.sleep(3)

l298n1.back()
l298n2.forward()
time.sleep(3)

GPIO.cleanup()
