import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
	while True:
		input_state = input()
		
		if input_state == 1:
			GPIO.output(17, GPIO.HIGH)
			print('Luz encendida')
			time.sleep(1)
		else:
			GPIO.output(17, GPIO.LOW)
			print('Luz apagada')
			time.sleep(1)

finally:
	GPIO.output(17, GPIO.LOW)
	GPIO.cleanup()
	print('Finalizado')
