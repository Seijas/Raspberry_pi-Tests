import RPi.GPIO as GPIO
import time

print("Gpio a utilizar")
number_gpio = input()

GPIO.setmode(GPIO.BCM)
GPIO.setup(number_gpio, GPIO.IN)

try:
	while True:
		print(GPIO.input(number_gpio))
		time.sleep(0.5)

finally:
	GPIO.cleanup()
	print('FINALIZADO')

