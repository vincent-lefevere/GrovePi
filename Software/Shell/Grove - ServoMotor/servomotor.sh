#!/bin/bash

# I2C addresses
GroveAddresse=0x04

# Servomotor Command
ServoCmd=101
ServoParamCmd=100

function servoAttach()
{
  i2cset -y 1 $GroveAddresse $ServoCmd $1 0x00 0x00 i
}

function servoDetach()
{
  i2cset -y 1 $GroveAddresse $ServoCmd $1 0x02 0x00 i
}

function servoWrite()
{
  i2cset -y 1 $GroveAddresse $ServoCmd $1 0x01 $2 i
}

