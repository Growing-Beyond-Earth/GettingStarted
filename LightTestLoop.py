# GROWNG BEYOND EARTH CONTROL BOX Traning
# RASPBERRY PI PICO / MICROPYTHON

# FAIRCHILD TROPICAL BOTANIC GARDEN, Oct 18, 2021

# The Growing Beyond Earth (GBE) control box is a device that controls
# the LED lights and fan in a GBE growth chamber. It can also control
# accessories including a 12v water pump and environmental sensors. 
# The device is based on a Raspberry Pi Pico microcontroller running 
# Micropython.
# lesson Written by @MarioTheMaker  



from sys import stdin, stdout, exit
import machine
import time

#Set the brightness for each color 
red_brightness = 100
green_brightness = 100
blue_brightness = 100
white_brightness = 100

# Pulse width modulation (PWM) is a way to get an artificial analog output on a digital pin.
# It achieves this by rapidly toggling the pin from low to high. There are two parameters
# associated with this: the frequency of the toggling, and the duty cycle.
# The duty cycle is defined to be how long the pin is high compared with the length of a
# single period (low plus high time). Maximum duty cycle is when the pin is high all of the
# time, and minimum is when it is low all of the time.
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7#:

# control I/O pins
# machine.Pin(id, mode=- 1, pull=- 1, *, value, drive, alt)
# Access the pin peripheral (GPIO pin) associated with the given id.
# If additional arguments are given in the constructor then they are used to initialise
# the pin. Any settings that are not specified will remain in their previous state.
# More info https://docs.micropython.org/en/latest/library/machine.Pin.html
r=machine.PWM(machine.Pin(0)); r.freq(20000)   # Red channel
g=machine.PWM(machine.Pin(2)); g.freq(20000)   # Green channel
b=machine.PWM(machine.Pin(1)); b.freq(20000)   # Blue channel
w=machine.PWM(machine.Pin(3)); w.freq(20000)   # White channel


# More info https://docs.micropython.org/en/latest/library/machine.PWM.html
# Start a loop and change the brightness multiplier "n"
# PWM.duty_u16([value]) Get the current duty cycle of the PWM output,
# as an unsigned 16-bit value in the range 0 to 65535 inclusive.
n = 100
while n > 0:
    print("Power Level ",n)
    r.duty_u16(int(red_brightness)*n)
    g.duty_u16(int(green_brightness)*n)
    b.duty_u16(int(blue_brightness)*n)
    w.duty_u16(int(white_brightness)*n)
    time.sleep(.3)
    n = n - 5
 
#Turn all the lights off
time.sleep(3)
r.duty_u16(0)
g.duty_u16(0)
b.duty_u16(0)
w.duty_u16(0)
