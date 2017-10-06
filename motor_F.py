# Importamos las librerias necesarias
import RPi.GPIO as GPIO
import time

# Definicion de variables
PWM = 21 # El puerto GPIO 21
M1 = 20  # El puerto GPIO 20
M2 = 16  # EL puerto GPIO 16

# Configuracion de puertos
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM, GPIO.OUT)
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)

# Incializar el sistema
PWM = GPIO.PWM(PWM,100) # Inicializar un PWN con 100 pulsos por segundo
PWM.start(50) # Arranque de la senal PWM al 50 %

# Arranque del PWW sentido hacia delante

GPIO.output(M1, GPIO.LOW)
GPIO.output(M2, GPIO.HIGH)

for i in range(0,5):
	time.sleep(1)

GPIO.cleanup()
#FIN


