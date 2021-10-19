# GROWNG BEYOND EARTH CONTROL BOX Traning
# RASPBERRY PI PICO / MICROPYTHON

# FAIRCHILD TROPICAL BOTANIC GARDEN, October 18, 2021

# The Growing Beyond Earth (GBE) control box is a device that controls
# the LED lights and fan in a GBE growth chamber. It can also control
# accessories including a 12v water pump and environmental sensors. 
# The device is based on a Raspberry Pi Pico microcontroller running 
# Micropython.
# lesson Written by @MarioTheMaker

from time import sleep

def print_thirteen_times_table_until(stop_at = 38):
    n = 0

    while n < stop_at:
        print(f"13 x {n} = {13*n}")
        n = n+1
        sleep(0.5)

    print(f"n = {n} which is no longer less than {stop_at}")
    return n


print("Calling Function...")
print_thirteen_times_table_until()
# print_thirteen_times_until(5)
# print_thirteen_times_until(stop_at = 5)
# n = print_thirteen_times_until(5.7)
print("End")
