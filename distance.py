import RPi.GPIO as GPIO
import time
import car

GPIO.cleanup()

trigger_pin = 18
echo_pin = 23
GPIO.setmode(GPIO.BCM)

GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)

def send_trigger_pulse():
    GPIO.output(trigger_pin,GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(trigger_pin,GPIO.LOW)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(GPIO.HIGH,10000)
    start = time.time()
    wait_for_echo(GPIO.LOW,10000)
    finish = time.time()
    pulse_len = finish - start
    distance = pulse_len / 0.000058
    return distance

	
	

car = car.Car2Wheel([12,16,20,21],GPIO.LOW)

car.lunch()

car.test()
	
car.forward()

try:
	while True:	
		if get_distance()<40:
			car.turn_left(50)
			time.sleep(0.1)
			car.forward()
except:
	GPIO.cleanup()
	
