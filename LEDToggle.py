# GROWNG BEYOND EARTH CONTROL BOX Traning
# RASPBERRY PI PICO / MICROPYTHON

# FAIRCHILD TROPICAL BOTANIC GARDEN, October 18, 2021

# The Growing Beyond Earth (GBE) control box is a device that controls
# the LED lights and fan in a GBE growth chamber. It can also control
# accessories including a 12v water pump and environmental sensors. 
# The device is based on a Raspberry Pi Pico microcontroller running 
# Micropython.
# lesson Written by @MarioTheMaker

from machine import Pin
led = Pin(6, Pin.OUT)

led.toggle()
