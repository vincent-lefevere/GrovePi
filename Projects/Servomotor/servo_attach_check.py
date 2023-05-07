from grovepi import *

for pin in range(11):
	print("pin = ",pin)
	print(servoAttached(pin))
	servoAttach(pin)
	print(servoAttached(pin))
	servoDetach(pin)
	print(servoAttached(pin))
	print()

