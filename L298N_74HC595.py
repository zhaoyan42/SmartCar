import RPi._GPIO as GPIO
from ic_74hc595.ic_74hc595 import IC_74HC595 as IC_74HC595

class L298N_74HC595(object):
    '''
    This Class is the Controller of 2*L298N by 1*74HC595
    '''

    __ic_74hc595 = None

    def __init__(self,pins,real_true = GPIO.HIGH):
        '''
        Init the leds
        :param pin: pin numbers in array
        :param real_true: GPIO.HIGH or GPIO.LOW
        :return: void
        '''
        self.__ic_74hc595 = IC_74HC595(pins,real_true)
        for name,number in pins.items():
            GPIO.setup(number,GPIO.OUT)

    @property
    def ic(self):
        return self.__ic_74hc595
    
    '''Test only all HIGH'''
    def on(self):
        self.ic.set_data(0xff)

    '''Test only all LOW'''
    def off(self):
        self.ic.set_data(0x00)

    def forward(self):
        self.ic.set_data(0xAA)

    def back(self):
        self.ic.set_data(0x55)
    
    
import time

GPIO.setmode(GPIO.BCM)

a = L298N_74HC595({'ds':6,'shcp':19,'stcp':13},GPIO.HIGH)
a.forward()
time.sleep(2)
a.back()
time.sleep(2)
a.forward()
time.sleep(2)
a.back()
time.sleep(2)

a.off()

GPIO.cleanup()
