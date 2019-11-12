import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)

button = 4

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
        print ("HIGH")
    else:
        print ("LOW")
    time.sleep(0.5)
    