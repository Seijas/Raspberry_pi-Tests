import RPi.GPIO as GPIO
import time

gpi = 21
sle = 0.005

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpi, GPIO.OUT)

try:
    while True:

        GPIO.output(gpi, GPIO.HIGH)
        time.sleep(sle)

        GPIO.output(gpi, GPIO.LOW)
        time.sleep(sle)

finally:
    GPIO.output(gpi, GPIO.LOW)
    GPIO.cleanup()
    print('FIN DEL PROGRAMA')
