from multiprocessing import Process
import RPi.GPIO as GPIO
import time
buzz_pin=4
led_pin=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_pin, GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
start=time.time()
def led():
    global start
    while True:
	GPIO.output(led_pin,GPIO.HIGH)
	time.sleep(3)
        GPIO.output(led_pin,GPIO.LOW)
	time.sleep(3)
def buzzer():
    global start
    while True:
	GPIO.output(buzz_pin,GPIO.HIGH)
        time.sleep(3)
	GPIO.output(buzz_pin,GPIO.LOW)
        time.sleep(3)

if __name__=='__main__':
    Process(target=led).start()
    Process(target=buzzer).start()
