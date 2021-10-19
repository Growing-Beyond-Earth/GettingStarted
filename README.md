# Thonny IDE with the Raspberry Pi Pico

In this first lesson, we demonstrate how to use Thonny IDE and MicroPython on a Raspberry Pi Pico to do something simple with the Raspberry Pi Pico.

## Setup the environment

Let's begin by downloading and installing [Thonny Python IDE for beginners ](https://thonny.org/).

Once Thonny is installed, connect the Raspberry Pi Pico to the computer via the USB cable. When you start Thonny it should detect the Pico.

<img width="480" alt="USB" src="https://user-images.githubusercontent.com/1426877/137810102-ff0c4ffd-cd28-4c82-b689-bbe59cab93dd.jpeg"> <img width="480" alt="USB/GBE" src="https://user-images.githubusercontent.com/1426877/137810163-8d4aaa12-0de8-4751-a105-00ea4aa79e26.jpeg">

In the Thonny Tools menu, select "options", then "interpreter", and change the interpreter to the "MicroPython (Raspberry Pi Pico)" option. Also select the correct connection port for the device.
![Thonny-IDE-with-Raspberry-Pi-Pico-usb](https://user-images.githubusercontent.com/1426877/137755071-c7339229-fb2e-4d3b-bef7-818c0e9dab30.jpeg)

The Raspberry Pi Pico comes with MicroPython already flashed. This means that it is literally "plug and play"

## Documentation

You can find information about the Raspberry Pi Pico on the  [Pico web page](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html).  The Raspberry Pi Pico is well-equipped with all sorts of GPIO and communication capabilities.

## Lesson #1: Hello World

Create a new script with `File>New` and paste in the following code:

```python
print("Hello, World!")
```

Click the green play button to run the code. Thonny will ask where to save the code to. Select `Raspberry Pi Pico` and name the file lesson1.py.

<img width="1068" alt="SavePico" src="https://user-images.githubusercontent.com/1426877/137758143-fb010874-a2ba-4475-b0c4-9c2bd010cc88.png">

We see the effect of the print statement in Thonny's console, but the actual "logic" is running on the Pico.  This distinction will become more apparent in later lessons when we write code that interacts with things other than the console (lights, sensors, external displays, etc).

## Lesson #2: Printing, Variables, Sleeping, Looping

In this lesson we will use our first module. The `time` module provides functions for getting the current time and date, and for "sleeping" (waiting around doing nothing).

Let's create a new script with `File>New` and paste in the following code:

```python
from time import sleep

n = 0

while True:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)
```

Click the green play button to run the code and save it as `lesson2.py`

This program initializes the variable `n=0` and then enters a while loop, where it print the thirteen-times table.

Python is unlike other programming languages in that the **whitespace is part of the syntax**. In the code above, the lines below the `while True:` line are indented to indicate that they will be executed repeatedly-- as long as "while clause" is `True`.
In our case, the while clause is simply the expression `True`.  Since `True` is always `True`, our program will never leave the while loop and will never terminate naturally.
Each time through the loop, we print `13 x n` and then make `n` one larger. Pressing the red stop button or typing `ctrl + C` in the console will send an interupt signal to the program, forcing it to terminate.  

Python has two primitive loop commands:

- `while`  loops
- `for`  loops

We will come back to `for` loops later.
For now, let's suppose we want to stop our program after we printed `13 x 37`. How could we do that?
In order to exit the `while` loop, the while clause (everything between the word `while` and the colon) will eventually need to be `False`.  

```python
from time import sleep

n = 0

while n < 38:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)
 ```

What is the value of `n` at the moment right before this program ends? We can check by adding another `print`:

```python
from time import sleep

n = 0

while n < 38:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)

print(f"n now has value {n} and our program is complete!")
```

Notice that this last `print` line is *outside* of the `while` loop-- it is not indented and will only be executed once the while clause is `False`.  We also used an [f string](https://realpython.com/python-f-strings/).  The `f` before the quotes on a string indicate that anything inside `{}` should be evaluated and printed.  There are several different syntaxes in python for formatting strings, but `f` strings are quite eligent.  Be warned however-- they were introduced in python `3.6` and will not work in older versions of python.

## Lesson #3: Functions and Comments

Create a new script with `File>New` and paste in the following code:

 ```python
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
```

Click the green play button to run the and save it as lesson3.py

*Functions* are blocks of code that are referred to by name. Functions can take in *positional arguments* or *keyword arguments* or both.  They can optionally return data (the return value). In the function definition *default values* can also be assigned to arguments.

Any code between a `#` and the end of the line it is on is called a *comment*.  We put comments in the code for humans-- the python interpreter ignores them completely.  Try toggling on and off the commented lines in `lesson3.py` and running the code to see how the function `print_thirteen_times_until` responds to different arguements being passed in.

## Lesson #4: (Optional Advanced topics) Dynamic Typing, `range`, and List Comprehensions

At the end of the last lesson we did something unexpected-- we passed the decimal number 5.7 to our function `print_thirteen_times_until`.  When we were writing the function we probably anticipated the arguement `stop_at` always being an `Integer`-- after all, who stops counting at a decimal? But Python has no problem knowing that the integers 0,1,2,3,4, 5 are all less than the decimal 5.7, so the program continued to execute and didn't raise any errors.  Is this a blessing or a curse?  A feature or a bug?  

Create a new script with `File>New` and paste in the following code:

 ```python

# the + operator in python is overloaded!
print(3+5)
print(type(3), type(5), type(3+5))

print(3+5.0)
print(type(3), type(5.0), type(3 + 5.0))

print("3" + "5")
print(type(3), type(5), type("3" + "5"))

print([1,2,3]+[4,5])
print(type([1,2,3]), type([4,5]), type([1,2,3]+[4,5]))

#what is range?
print(range(5))

# range(stop)
for i in range(5):
    print(i)

#range(start, stop)
range_as_list = [i for i in range(3, 10)]
print(range_as_list)

# range(start, stop, step)
print([i for i in range(3, 5, .5)])
```

Click the green play button to run the and save it as lesson4.py

Here we see the highly dynamic nature of Python.  We add integers and get an integer.  We add an integer and a float, and get a float.  
Add strings to get concatenated strings.  Add lists to get concatenated lists.

Checkout these links for more details on the builtin function [range](https://www.w3schools.com/python/ref_func_range.asp) and [list comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp)

## Capstone: GPIO

Now let's start working with the Control box.

![IMG_4519](https://user-images.githubusercontent.com/1426877/137814836-7e92faf8-b270-49fd-b2f4-61e9a0277072.jpeg)


GPIO Pins
The way to control  other components, is through the GPIO pins. Not all pins are available to use.

The pins are available in the machine module, so make sure you import that first.
let's define led to the pin
let's toggle the led

Create a new script with `File>New` and paste in the following code:

```python
from machine import Pin
led = Pin(6, Pin.OUT)

led.toggle()
```

Click the green play button to run the and save it as `LEDToggle.py`
Every time you the the Run button the led should toggle on or off.

Lets modify this code a little with what we have learned all ready:

  ```python
from machine import Pin
from time import sleep


led = Pin(6, Pin.OUT)
n=0

led.toggle()

while n < 8:
    led.toggle()
    n = n+1
    sleep(0.5)

else:
  print("Done toggling ")
 ```

What does this new example do ?

The LED should be toggling on and off. 

Now lets make the LED fade in and out using Pulse width modulation (PWM). Moving foward all the examples will have the expxlantion in the code. 
Now let's make the LED fade in and out using Pulse width modulation (PWM);


In order to use PWM in MicroPython, we will use just three instructions:
```
from machine import Pin , PWM
pwm = PWM  (  Pin  (  16  )  ) # GPIO # 
pwm. freq  (  100000  ) # 100kHz Frequency 

```
The test code above, should generate a 100kHz PWM signal with a 50% duty cycle on pin 16

PWM Pulse width modulation allows you control devices, such as motors and lamps,LED's. This means that rather than the motor/lamp being simply on or off, 
This means that rather than the motor/lamp being simply on or off, you can regulate its speed or brightness.


Create a new script with File>New and paste in the following code:
Let’s use the PWM feature to fade an LED

```python
from machine import Pin, PWM
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
# Access the pin peripheral (GPIO pin) associated with the given id.
# If additional arguments are given in the constructor then they are used to initialise
# the pin. Any settings that are not specified will remain in their previous state.
# More info https://docs.micropython.org/en/latest/library/machine.Pin.html

# Construct PWM object, with LED on Pin(6) pin used on the GBE Box.
pwm = PWM(Pin(6))

# Set the PWM frequency.
pwm.freq(1000)

#Start Loop

#FadeIn
while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
#FadeOut
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)


```

Click the green play button to run the and save it as `PWM-LED.py`

## Controling the GBE light pannel 

Now that we undestand PWM lets control the Red LEDs lights on the GBE box light pannel 

![FAOiOaJVQAgzIez](https://user-images.githubusercontent.com/1426877/137812924-6f1ab3f4-2bfb-4634-a012-9b73efbdb6d2.jpeg)

Create a new script with `File>New` and paste in the following code:

```
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
#Green Lights Pin(2)
#Blue Lights  Pin(3)
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
```
Click the Green Play button to Run the and save it as PWM-RedLED.py


Now lets control all the lights on the GBE box 
Create a new script with `File>New` and paste in the following code:

```
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
#Set the power level 
n = 200
#lets turn all the lights on and reduce the power by 5 as we loop trough it till power gets to zero. 
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
```

Click the Green Play(Run) button to Run the and save it as LightTestLoop.py


## Controling the GBE fan

Create a new script with `File>New` and paste in the following code:

```
import machine
from time import sleep
# control I/O pins
# machine.Pin(id, mode=- 1, pull=- 1, *, value, drive, alt)
#Pin for the GBE FAN
#Pin(40)
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
```

















**NOTE: If you wish to run the code automatically whenever you power Raspberry Pi Pico then you have to name your code file as `main.py` while saving it.**

## Raspberry Pi Pico Python SDK

[Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) book published by Raspberry Pi Trading,
which forms part of the technical documentation in support of Raspberry Pi Pico and the MicroPython port to RP2040.

## MicroPython Documentation

[MicroPython 1.7](https://docs.micropython.org/en/latest/index.html)

## More with MicroPython on Raspberry Pi Pico

For more physical computing projects to try on your Raspberry Pi Pico, grab a copy of the new book, Get Started with MicroPython on Raspberry Pi Pico.
As well as learning how to use Raspberry Pi Pico’s pins as inputs and outputs, you’ll build a simple game, measure temperatures, save and load data to
your Pico’s file system, and even make a burglar alarm for your room.

[Get Started with MicroPython on Raspberry Pi Pico is available now from Raspberry Pi Press](https://magpi.cc/picobook).
