import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, GPIO.PUD_UP)
try:
    while True:
        button_state1 = GPIO.input(22)
        button_state2 = GPIO.input(23)
        button_state3 = GPIO.input(24)
        if button_state1 == GPIO.LOW:
            GPIO.output(4,GPIO.HIGH)
        if button_state2 == GPIO.LOW:
            GPIO.output(17,GPIO.HIGH)
        if button_state3 == GPIO.LOW:
            GPIO.output(27,GPIO.HIGH)
        if button_state1 == GPIO.LOW and button_state2 == GPIO.LOW and button_state3 == GPIO.LOW:
            GPIO.output(4,GPIO.LOW)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(4,GPIO.LOW)
            time.sleep(1)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(17,GPIO.LOW)
            time.sleep(1)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27,GPIO.LOW)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(4,GPIO.LOW)
            time.sleep(1)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(17,GPIO.LOW)
            time.sleep(1)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27,GPIO.LOW)
        else:
            GPIO.output(4,GPIO.LOW)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
except KeyboardInterrupt:
   GPIO.cleanup()
finally:
    GPIO.cleanup()