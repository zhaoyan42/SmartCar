import RPi.GPIO as GPIO
import time

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

while True:
    print(get_distance())
    time.sleep(0.1)
