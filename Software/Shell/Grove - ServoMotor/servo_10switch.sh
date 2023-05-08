#!/bin/bash

. servomotor.sh

pin=5

servoAttach $pin
for i in 0 1 2 3 4 5 6 7 8 9
do
  servoWrite $pin 0
  sleep 1
  servoWrite $pin 180
  sleep 1
done
servoDetach $pin

