import RPi.GPIO as GPIO
import time

class Motor(object):
    '''
    This Class is a Motor Controlled by GPIO pins
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


class SmartCar(object):
    '''
    This class is a driver control all Motors
    '''

    f_l_motor = None
    f_r_motor = None
    b_l_motor = None
    b_r_motor = None

    def __init__(self,motor_pins,real_true = GPIO.HIGH):
        self.f_l_motor = Motor(motor_pins[0],motor_pins[1],real_true)
        self.f_r_motor = Motor(motor_pins[2],motor_pins[3],real_true)
        self.b_l_motor = Motor(motor_pins[4],motor_pins[5],real_true)
        self.b_r_motor = Motor(motor_pins[6],motor_pins[7],real_true)

    @property
    def f_motors(self):
        return [self.f_l_motor,self.f_r_motor]

    @property
    def b_motors(self):
        return [self.b_l_motor,self.b_r_motor]

    @property
    def r_motors(self):
        return [self.f_r_motor,self.b_r_motor]

    @property
    def l_motors(self):
        return [self.f_l_motor,self.b_l_motor]

    @property
    def all_motors(self):
        return [self.f_l_motor,self.f_r_motor,self.b_l_motor,self.b_r_motor]

    def lunch(self):
        for motor in self.all_motors:
            motor.lunch()

    def test(self):
        for motor in self.all_motors:
            motor.positive_rotation()
            time.sleep(0.5)
            motor.negative_rotation()
            time.sleep(0.5)
            motor.stop()

    def forward(self,speed_persent):
        for motor in self.all_motors:
            motor.positive_rotation(speed_persent)

    def backward(self,speed_persent):
        for motor in self.all_motors:
            motor.negative_rotation(speed_persent)

    def rotate_left(self,speed_persent):
        self.f_l_motor.negative_rotation(speed_persent)
        self.f_r_motor.positive_rotation(speed_persent)
        self.b_l_motor.negative_rotation(speed_persent)
        self.b_r_motor.positive_rotation(speed_persent)

    def rotate_right(self,speed_persent):
        self.f_l_motor.positive_rotation(speed_persent)
        self.f_r_motor.negative_rotation(speed_persent)
        self.b_l_motor.positive_rotation(speed_persent)
        self.b_r_motor.negative_rotation(speed_persent)

    def turn_left(self,speed_persent):
        self.f_l_motor.negative_rotation(speed_persent*0)
        self.f_r_motor.positive_rotation(speed_persent)
        self.b_l_motor.negative_rotation(speed_persent)
        self.b_r_motor.positive_rotation(speed_persent)

    def turn_right(self,speed_persent):
        self.f_l_motor.positive_rotation(speed_persent)
        self.f_r_motor.negative_rotation(speed_persent*0)
        self.b_l_motor.positive_rotation(speed_persent)
        self.b_r_motor.negative_rotation(speed_persent)


    def terminate(self):
        for motor in self.all_motors:
            motor.terminate()

    def stop(self):
        for motor in self.all_motors:
            motor.stop()

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

car = SmartCar([24,25,18,23,12,16,20,21],GPIO.LOW)

car.lunch()
car.rotate_left(50)
time.sleep(1)
car.rotate_right(50)
time.sleep(1)
car.turn_left(50)
time.sleep(1)
car.turn_right(50)
time.sleep(1)
car.stop()
car.terminate()

GPIO.cleanup()
