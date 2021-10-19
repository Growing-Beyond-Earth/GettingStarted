
# GROWNG BEYOND EARTH CONTROL BOX Traning
# RASPBERRY PI PICO / MICROPYTHON

# FAIRCHILD TROPICAL BOTANIC GARDEN, October 18, 2021

# The Growing Beyond Earth (GBE) control box is a device that controls
# the LED lights and fan in a GBE growth chamber. It can also control
# accessories including a 12v water pump and environmental sensors. 
# The device is based on a Raspberry Pi Pico microcontroller running 
# Micropython.
# lesson Written by MarioTheMaker 



from sys import stdin, stdout, exit
import machine
import time
from time import sleep
#Set the brightness for each color 
red_brightness = 100
# Pulse width modulation (PWM) is a way to get an artificial analog output on a digital pin.
# It achieves this by rapidly toggling the pin from low to high. There are two parameters
# associated with this: the frequency of the toggling, and the duty cycle.
# The duty cycle is defined to be how long the pin is high compared with the length of a
# single period (low plus high time). Maximum duty cycle is when the pin is high all of the
# time, and minimum is when it is low all of the time.
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7#:

# control I/O pins
# machine.Pin(id, mode=- 1, pull=- 1, *, value, drive, alt)
#Pins for the GBE light panel 
#Red Lights   Pin(0)
#Green Lights Pin(1)
#Blue Lights  Pin(2)
#White Lights  Pin(3)

r=machine.PWM(machine.Pin(0)); r.freq(20000)   # Setup the Red channel on Pin0
n=100
while n > 0:
    print("Power Level",n)
    r.duty_u16(int(red_brightness)*n)
    n = n - 15
    sleep(0.5)
    
else:
    print("turn the Red LED off")
    r.duty_u16(0) #turn it off 
