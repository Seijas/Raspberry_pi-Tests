import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

try:
	while True:
		input_state = GPIO.input(18)
		print(input_state)

		if input_state == True:
			GPIO.output(17, GPIO.HIGH)
			print('Luz encendida')
			time.sleep(1)
		else:
			GPIO.output(17, GPIO.LOW)
			print('Luz apagada')
			time.sleep(1)
finally:
	print('Fuera')
	GPIO.output(17, GPIO.LOW)
	GPIO.cleanup()
	print('Terminado')
