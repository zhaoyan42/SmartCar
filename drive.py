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
    __pwm1 = None
    __pwm2 = None
    __pwm3 = None
    __pwm4 = None
    __pwm_frequncy = 10000
    __real_true = GPIO.HIGH

    def __init__(self,in1,in2,in3,in4,real_true = GPIO.HIGH):
        self.__in1 = in1
        GPIO.setup(self.__in1,GPIO.OUT)
        self.__pwm1 = GPIO.PWM(self.__in1,self.__pwm_frequncy)

        self.__in2 = in2
        GPIO.setup(self.__in2,GPIO.OUT)
        self.__pwm2 = GPIO.PWM(self.__in2,self.__pwm_frequncy)

        self.__in3 = in3
        GPIO.setup(self.__in3,GPIO.OUT)
        self.__pwm3 = GPIO.PWM(self.__in3,self.__pwm_frequncy)

        self.__in4 = in4
        GPIO.setup(self.__in4,GPIO.OUT)
        self.__pwm4 = GPIO.PWM(self.__in4,self.__pwm_frequncy)

        self.__real_true = real_true

    def lunch(self):        
        self.__pwm1.start(0)
        self.__pwm2.start(0)
        self.__pwm3.start(0)
        self.__pwm4.start(0)

    def forward(self,duty_cycle = 100):
        self.__pwm1.ChangeDutyCycle(duty_cycle)
        self.__pwm2.ChangeDutyCycle(0)
        self.__pwm3.ChangeDutyCycle(duty_cycle)
        self.__pwm4.ChangeDutyCycle(0)   

    def back(self,duty_cycle = 100):
        self.__pwm1.ChangeDutyCycle(0)
        self.__pwm2.ChangeDutyCycle(duty_cycle)
        self.__pwm3.ChangeDutyCycle(0)
        self.__pwm4.ChangeDutyCycle(duty_cycle)

    def stop(self):
        self.__pwm1.ChangeDutyCycle(0)
        self.__pwm2.ChangeDutyCycle(0)
        self.__pwm3.ChangeDutyCycle(0)
        self.__pwm4.ChangeDutyCycle(0)

    def terminate(self):
        self.__pwm1.stop()
        self.__pwm2.stop()
        self.__pwm3.stop()
        self.__pwm4.stop()


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

l298n1 = L298N_GPIO(18,23,24,25)
l298n2 = L298N_GPIO(12,16,20,21)

l298n1.lunch()
l298n2.lunch()

for i in range(30,100):
    l298n1.forward(i)
    l298n2.forward(i)
    time.sleep(0.1)
time.sleep(2)

for i in range(30,100):
    l298n1.back(i)
    l298n2.back(i)
    time.sleep(0.1)
time.sleep(2)

l298n1.terminate()
l298n2.terminate()

GPIO.cleanup()
