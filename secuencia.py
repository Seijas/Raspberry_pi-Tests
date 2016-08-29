import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)	# SALIDA
GPIO.setup(18, GPIO.IN)		# ENTRADA SENAL
GPIO.setup(23, GPIO.IN)		# ENTRADA BOTON


input_senal = GPIO.input(18)
input_boton = GPIO.input(23)

list_towers = []

try:
	while True:
		while GPIO.input(23):
			# Grabamos secuancia
			print("escribiendo")
			list_towers.append(GPIO.input(18))
			time.sleep(0.05)

		while GPIO.input(23) == False:
			#reproducimos
			print("leyendo")
			for a in list_towers:
				print (a)

				if a == 1:
					GPIO.output(17, GPIO.HIGH)
				else:
					GPIO.output(17, GPIO.LOW)

				time.sleep(0.05)

			GPIO.output(17, GPIO.LOW)
			list_towers = []
			time.sleep(1)

finally:
	print('Cancelado')
	GPIO.output(17, GPIO.LOW)
	GPIO.cleanup()
	print('FIN DEL PROGRAMA')

