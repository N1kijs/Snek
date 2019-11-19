import smbus2
import bme280

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

port = 1
address = 0x76
bus = smbus2.SMBus(port)
claibration_params = bme280.load_calibration_params(bus, address)

try:
    while True:
        button_state1 = GPIO.input(22)
        button_state2 = GPIO.input(23)
        button_state3 = GPIO.input(24)
        data = bme280.sample(bus, address, claibration_params)
        if button_state1 == GPIO.LOW:
            GPIO.output(4,GPIO.HIGH)
            print(data.timestamp)
            time.sleep(0.4)
        if button_state2 == GPIO.LOW:
            GPIO.output(17,GPIO.HIGH)
            print(data.pressure)
            time.sleep(0.4)
        if button_state3 == GPIO.LOW:
            GPIO.output(27,GPIO.HIGH)
            print(data.temperature)
            time.sleep(0.4)
        else:
            GPIO.output(4,GPIO.LOW)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
except KeyboardInterrupt:
   GPIO.cleanup()
finally:
    GPIO.cleanup()

