import RPi.GPIO as GPIO

class Wheel(object):
    '''
    This Class is a Wheel Controlled by GPIO pins
    '''

    __in1 = 0
    __in2 = 0
    __pwm1 = None
    __pwm2 = None
    __pwm_frequncy = 50
    __real_true = GPIO.HIGH

    def __init__(self,in1,in2,real_true = GPIO.HIGH):
        self.__in1 = in1
        GPIO.setup(self.__in1,GPIO.OUT)
        self.__pwm1 = GPIO.PWM(self.__in1,self.__pwm_frequncy)

        self.__in2 = in2
        GPIO.setup(self.__in2,GPIO.OUT)
        self.__pwm2 = GPIO.PWM(self.__in2,self.__pwm_frequncy)

        self.__real_true = real_true

    def lunch(self):        
        self.__pwm1.start(0)
        self.__pwm2.start(0)

    def positive_rotation(self,duty_cycle = 100):    
        if self.__real_true:
            self.__pwm1.ChangeDutyCycle(duty_cycle)
            self.__pwm2.ChangeDutyCycle(0)
        else:
            self.__pwm1.ChangeDutyCycle(0)
            self.__pwm2.ChangeDutyCycle(duty_cycle)
   
    def negative_rotation(self,duty_cycle = 100):
        if self.__real_true:
            self.__pwm1.ChangeDutyCycle(0)
            self.__pwm2.ChangeDutyCycle(duty_cycle)
        else: 
            self.__pwm1.ChangeDutyCycle(duty_cycle)
            self.__pwm2.ChangeDutyCycle(0)

    def stop(self):
        self.__pwm1.ChangeDutyCycle(0)
        self.__pwm2.ChangeDutyCycle(0)

    def terminate(self):
        self.__pwm1.stop()
        self.__pwm2.stop()

