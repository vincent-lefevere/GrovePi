import time
from grovepi import *

servomotor0_pin = 6		#Port for servomotor0
servoAttach(servomotor0_pin)
while True:
	try:
		v=0
		while v<=180:
			servoWrite(servomotor0_pin,v)
			time.sleep(0.040)
			print(servoRead(servomotor0_pin))
			v+=1
		v=180
		while v>=0:
			servoWrite(servomotor0_pin,v)
			time.sleep(0.040)
			print(servoRead(servomotor0_pin))
			v-=1
	except KeyboardInterrupt:
		servoDetach(servomotor0_pin)
		break
	except (IOError,TypeError) as e:
		print("Error")
