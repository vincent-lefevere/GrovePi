import time
from grovepi import *

servomotor0_pin = 6		#Port for servomotor0
servoAttach(0,servomotor0_pin)
while True:
	try:
		v=0
		while v<=180:
			servoWrite(0,v)
			time.sleep(0.040)
			v+=1
		v=180
		while v>=0:
			servoWrite(0,v)
			time.sleep(0.040)
			v-=1
	except KeyboardInterrupt:
		servoDettach(0,servomotor0_pin)
		break
	except (IOError,TypeError) as e:
		print("Error")
