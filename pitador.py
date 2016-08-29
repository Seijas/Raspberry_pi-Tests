import RPi.GPIO as GPIO
import time

gpi = 21
sle = 0.001

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpi, GPIO.OUT)

try:
    e = 1

    while True:

        if e == 1:
            e = 2
            GPIO.output(gpi, GPIO.HIGH)
            time.sleep(sle)
        else:
            e = 1
            GPIO.output(gpi, GPIO.LOW)
            time.sleep(sle)

finally:
    print('Cancelado')
    GPIO.output(gpi, GPIO.LOW)
    GPIO.cleanup()
    print('FIN DEL PROGRAMA')
