import time
from grovepi import *

servomotor0_pin = 5		#Port for servomotor0

while True:
	try:
		v=int(input("valeur entre 0 et 180 ? "))
		servoAttach(0,servomotor0_pin)
		servoWrite(0,v)
		time.sleep(0.500)
		servoDettach(0,servomotor0_pin)
	except KeyboardInterrupt:
		servoDettach(0,servomotor0_pin)
		break
	except (IOError,TypeError) as e:
		print("Error")
