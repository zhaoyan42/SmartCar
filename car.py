import RPi.GPIO as GPIO
from abc import ABCMeta,abstractmethod
import wheel as wheel
import time


class Car(object):
    __metaclass__ = ABCMeta

    @property
    def all_wheels(self):
        pass

    def lunch(self):
        for wheel in self.all_wheels:
            wheel.lunch()

    def terminate(self):
        for wheel in self.all_wheels:
            wheel.terminate()

    def stop(self):
        for wheel in self.all_wheels:
            wheel.stop()

    def forward(self,speed_persent=100):
        for wheel in self.all_wheels:
            wheel.positive_rotation(speed_persent)

    def backward(self,speed_persent=100):
        for wheel in self.all_wheels:
            wheel.negative_rotation(speed_persent)

    def test(self):
        for wheel in self.all_wheels:
            wheel.positive_rotation()
            time.sleep(0.5)
            wheel.negative_rotation()
            time.sleep(0.5)
            wheel.stop()

class Car2Wheel(Car):
    '''
    This class is a driver control all Wheels
    '''

    b_l_wheel = None
    b_r_wheel = None

    def __init__(self,wheel_pins,real_true = GPIO.HIGH):
        self.b_l_wheel = wheel.Wheel(wheel_pins[0],wheel_pins[1],real_true)
        self.b_r_wheel = wheel.Wheel(wheel_pins[2],wheel_pins[3],real_true)

    @property
    def all_wheels(self):
        return [self.b_l_wheel,self.b_r_wheel]

    def turn_left(self,speed_persent=100):
        self.b_l_wheel.negative_rotation(speed_persent)
        self.b_r_wheel.positive_rotation(speed_persent)

    def turn_right(self,speed_persent=100):
        self.b_l_wheel.positive_rotation(speed_persent)
        self.b_r_wheel.negative_rotation(speed_persent)



class Car4Wheel(Car):
    '''
    This class is a driver control all Wheels
    '''

    f_l_wheel = None
    f_r_wheel = None
    b_l_wheel = None
    b_r_wheel = None

    def __init__(self,wheel_pins,real_true = GPIO.HIGH):
        self.f_l_wheel = wheel.Wheel(wheel_pins[0],wheel_pins[1],real_true)
        self.f_r_wheel = wheel.Wheel(wheel_pins[2],wheel_pins[3],real_true)
        self.b_l_wheel = wheel.Wheel(wheel_pins[4],wheel_pins[5],real_true)
        self.b_r_wheel = wheel.Wheel(wheel_pins[6],wheel_pins[7],real_true)

    @property
    def f_wheels(self):
        return [self.f_l_wheel,self.f_r_wheel]

    @property
    def b_wheels(self):
        return [self.b_l_wheel,self.b_r_wheel]

    @property
    def r_wheels(self):
        return [self.f_r_wheel,self.b_r_wheel]

    @property
    def l_wheels(self):
        return [self.f_l_wheel,self.b_l_wheel]

    @property
    def all_wheels(self):
        return [self.f_l_wheel,self.f_r_wheel,self.b_l_wheel,self.b_r_wheel]


    def rotate_left(self,speed_persent=100):
        self.f_l_wheel.negative_rotation(speed_persent)
        self.f_r_wheel.positive_rotation(speed_persent)
        self.b_l_wheel.negative_rotation(speed_persent)
        self.b_r_wheel.positive_rotation(speed_persent)

    def rotate_right(self,speed_persent=100):
        self.f_l_wheel.positive_rotation(speed_persent)
        self.f_r_wheel.negative_rotation(speed_persent)
        self.b_l_wheel.positive_rotation(speed_persent)
        self.b_r_wheel.negative_rotation(speed_persent)

    def turn_left(self,speed_persent=100):
        self.f_l_wheel.negative_rotation(speed_persent*0)
        self.f_r_wheel.positive_rotation(speed_persent)
        self.b_l_wheel.negative_rotation(speed_persent)
        self.b_r_wheel.positive_rotation(speed_persent)

    def turn_right(self,speed_persent=100):
        self.f_l_wheel.positive_rotation(speed_persent)
        self.f_r_wheel.negative_rotation(speed_persent*0)
        self.b_l_wheel.positive_rotation(speed_persent)
        self.b_r_wheel.negative_rotation(speed_persent)


