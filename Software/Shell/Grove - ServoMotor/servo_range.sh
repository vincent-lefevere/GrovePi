#!/bin/bash

# usage:
# ./servo_range.sh

. servomotor.sh

pin=5

servoAttach $pin
for n in 1 2 3 4 5 6 7 8
do
  i=0
  while test $i -ne 180
  do
    servoWrite $pin $i
    i=$(expr $i + 1)
  done
  while test $i -ne 0
  do
    servoWrite $pin $i
    i=$(expr $i - 1)
  done
done
servoDetach $pin

