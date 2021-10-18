# GROWNG BEYOND EARTH CONTROL BOX Traning
# RASPBERRY PI PICO / MICROPYTHON

# FAIRCHILD TROPICAL BOTANIC GARDEN, October 18, 2021

# The Growing Beyond Earth (GBE) control box is a device that controls
# the LED lights and fan in a GBE growth chamber. It can also control
# accessories including a 12v water pump and environmental sensors. 
# The device is based on a Raspberry Pi Pico microcontroller running 
# Micropython.
# lesson Written by MarioTheMaker 

import machine
from time import sleep

# Pulse width modulation (PWM) is a way to get an artificial analog output on a digital pin.
# It achieves this by rapidly toggling the pin from low to high. There are two parameters
# associated with this: the frequency of the toggling, and the duty cycle.
# The duty cycle is defined to be how long the pin is high compared with the length of a
# single period (low plus high time). Maximum duty cycle is when the pin is high all of the
# time, and minimum is when it is low all of the time.
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7#:

# control I/O pins
# machine.Pin(id, mode=- 1, pull=- 1, *, value, drive, alt)

#Pin for the GBE FAN
#Pin(40

fan_speed = 500
f=machine.PWM(machine.Pin(4)); f.freq(20000)   # Fan

n=100

while n > 0:
    print("fan_speed",n)
    f.duty_u16(fan_speed* 256)
    n = n - 15
    sleep(1)
    
else:
    print("turn the Fan off")
    f.duty_u16(0)

