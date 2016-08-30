import RPi.GPIO as GPIO

print("Gpio a utilizar")
gpi = input()

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpi, GPIO.OUT)

try:

    while True:

        print("Accion:")
        e = input()

        if e == 1:
            print("Alto")
            GPIO.output(gpi, GPIO.HIGH)
        else:
            print("Bajo")
            GPIO.output(gpi, GPIO.LOW)

finally:
    GPIO.output(gpi, GPIO.LOW)
    GPIO.cleanup()
    print('FINALIZADO')
