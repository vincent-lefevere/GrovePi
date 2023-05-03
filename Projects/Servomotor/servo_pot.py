import time
from grovepi import *

servomotor0_pin = 5		#Port D5 for servomotor0
potentiometer = 2       #Port A2 for potentiometer

servoAttach(0,servomotor0_pin)
while True:
	try:
		v=analogRead(potentiometer)
		v=int(v*180/1023)
		servoWrite(0,v)
		time.sleep(0.020)
	except KeyboardInterrupt:
		servoDettach(0,servomotor0_pin)
		break
	except (IOError,TypeError) as e:
		print("Error")
