import RPi.GPIO as GPIO

gpi = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpi, GPIO.IN)

try:

    while True:

        if GPIO.input(gpi) == True:
            print("Negro")
        else:
            print("Blanco")

finally:
    GPIO.cleanup()
    print('FIN DEL PROGRAMA')
