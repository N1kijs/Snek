import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

counter = 0
try:
    while counter < 30:
        print ("Led on")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        print ("Led off")
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
        print ("kkas jauns")
        counter = counter + 1
except KeyboardInterrupt :
    print ("\n"), counter
finally:
    GPIO.cleanup()