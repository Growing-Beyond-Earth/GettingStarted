# Thonny IDE with the Raspberry Pi Pico

In this lesson, I will demonstrate how to use Thonny IDE and MicroPython on a Raspberry Pi Pico to do something simple with the Raspberry Pi Pico, 
and your GBE control box. 

## Setup the environment
Let us begin by downloading and installing [Thonny Python IDE for beginners ](https://thonny.org/). 

Once Thonny is installed let us start by connecting the Raspberry Pi Pico inside the GBE Control box to the computer via the USB cable. 
Start Thonny and Thonny should detect the Raspberry Pi Pico.

<img width="480" alt="USB" src="https://user-images.githubusercontent.com/1426877/137810102-ff0c4ffd-cd28-4c82-b689-bbe59cab93dd.jpeg"> <img width="480" alt="USB/GBE" src="https://user-images.githubusercontent.com/1426877/137810163-8d4aaa12-0de8-4751-a105-00ea4aa79e26.jpeg">


In the Thonny Tools menu, select "options", then "interpreter", and change the interpreter to the "MicroPython (Raspberry Pi Pico)" option. 
Also select the correct connection port for the device.
![Thonny-IDE-with-Raspberry-Pi-Pico-usb](https://user-images.githubusercontent.com/1426877/137755071-c7339229-fb2e-4d3b-bef7-818c0e9dab30.jpeg)

The Raspberry Pi Pico comes with MicroPython already flashed. This means that it is literally "plug and play"

## Documentation

You can find information about the Raspberry Pi Pico on its  [Pico web page](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html). 
The Raspberry Pi Pico is well-equipped with all sorts of GPIO and communications capabilities.


## Writing a Python Script

Create a new script with File>New and paste in the following code:
```

print("Hello, World!")

```

Click the Green Play button to Run the code Thonny you will be prompted to save to your computer OR the pico. Select save to Pico and name the file lesson1.py

<img width="1068" alt="SavePico" src="https://user-images.githubusercontent.com/1426877/137758143-fb010874-a2ba-4475-b0c4-9c2bd010cc88.png">


lets create a new script with File>New and paste in the following code:
 ```
from time import sleep

n = 0

while True:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)
 ```
Click the Green Play button to Run the and save it as lesson2.py

Let see what the code does:
The time module provides functions for getting the current time and date, and for sleeping.

Python has two primitive loop commands:

-   while  loops
-   for  loops

we will us the While loop 
we set a variable n=0 and start a While loop and print the thirteen-times table until you hit the stop button

*For more information about loops https://realpython.com/python-while-loop/*

Now lets say you want to stop at 13x37 how do we do that?

```
from time import sleep

n = 0

while n < 38:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)
 ```
now it will stop when n gets to 38

now we will add the ```else``` statement it alows us to run a block of code once when the condition no longer is true:

lets add this to our code 
 ```
else:
  print("n is no longer less than 37")
 ```

The code should look like this 
```
from time import sleep

n = 0

while n < 38:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)

else:
  print("n is no longer less than 37")
```


Create a new script with File>New and paste in the following code:

 ```
from time import sleep


def therteentimes():
    n = 0

    while n < 38:
        print("13 x",n,"= ",13*n) # print the thirteen-times table
        n = n+1
        sleep(0.5)

    else:
        print("n is no longer less than 37")


print("Call Function")
therteentimes()
print("End")
```
Click the Green Play button to Run the and save it as lesson3.py



We taken what we have leanred and made the code a function we can call 
Functions are blocks of code that are referred to by name. Data can be passed into it to be operated on (i.e. the parameters) 
and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

Here is the same function passing in the times tabel we want "times" and the total of times "total" 

Create a new script with File>New and paste in the following code:
 ```
from time import sleep


def therteentimes(times,total):
    n = 0

    while n < total:
        print(times,"x",n,"= ",13*n) # print the times-times table
        n = n+1
        sleep(0.5)

    else:
        print("n is no longer less than",total)


print("Call Function")
therteentimes(3,10)
print("End of program")

```
Click the Green Play button to Run the and save it as lesson4.py


##Now lets start working with the Control box 

GPIO Pins
The way to control  other components, is through the GPIO pins. Not all pins are available to use.

The pins are available in the machine module, so make sure you import that first. 
lets define led to the pin
lets toggle the led

## Controling the GBE box LED 

![IMG_4519](https://user-images.githubusercontent.com/1426877/137814836-7e92faf8-b270-49fd-b2f4-61e9a0277072.jpeg)


Create a new script with File>New and paste in the following code:

```
from machine import Pin
led = Pin(6, Pin.OUT)

led.toggle()
```
Click the Green Play button to Run the and save it as LEDToggle.py

Every time you the the Run button the led should toggle on or off. 

Lets modify this code a little with what we have learned 
  ```
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
Click the Green Play button to Run

The LED should be toggling on and off. 

Now let's make the LED fade in and out using Pulse width modulation (PWM); as we move forward, 
the next best thing is to start commenting on your code. Again, moving forward, all the examples will have an explanation in the code. 

In order to use PWM in MicroPython, we will use just three instructions:
```
pwm = PWM  (  Pin  (  16  )  ) # GPIO # 

pwm. freq  (  100000  ) # 100kHz Frequency 

pwm. duty_u16  (  32768  ) # duty 50% (65535/2)

The duty cycle controls the pin’s output: a 0 percent duty cycle leaves the pin switched off for all 1000 pulses per
second, and effectively turns the pin off; a 100 percent duty cycle leaves the pin switched on for all 1000 pulses per second, and is 
functionally equivalent to just turning the pin on as a fixed digital output; a 50 percent duty cycle has the pin on for half the pulses 
and off for half the pulses.
```


If you run the test code  above, it should generate a 100kHz PWM signal with a 50% duty cycle on pin 16

PWM Pulse width modulation allows you to control devices, such as motors and lamps, LED. This means that rather than the motor/lamp being simply on or off, 
you can regulate its speed or brightness.

Create a new script with File>New and paste in the following code:

Let's use the PWM feature to fade an LED in and out

```
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
    for duty in range(65025): #100% Duty =65025
        pwm.duty_u16(duty)
        sleep(0.0001)
#FadeOut
    for duty in range(65025, 0, -1): #0% Duty =0
        pwm.duty_u16(duty)
        sleep(0.0001)


```
Click the Green Play button to Run the and save it as PWM-LED.py


## Controling the GBE box light pannel 

Now that we undestand PWM lets control the Red LEDs lights on the GBE box light pannel 

![FAOiOaJVQAgzIez](https://user-images.githubusercontent.com/1426877/137812924-6f1ab3f4-2bfb-4634-a012-9b73efbdb6d2.jpeg)


Create a new script with File>New and paste in the following code:

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


Now lers control all the lights on the GBE box 
Create a new script with File>New and paste in the following code:

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



**NOTE: If you wish to run the code automatically whenever you power Raspberry Pi Pico then you have to name your code file as "main.py" while saving it.**

## Raspberry Pi Pico Python SDK
"[Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) book published by Raspberry Pi Trading, 
which forms part of the technical documentation in support of Raspberry Pi Pico and the MicroPython port to RP2040.

## MicroPython 1.7 Documnetation 

MicroPython 1.7 https://docs.micropython.org/en/latest/index.html https://docs.micropython.org/en/latest/rp2/quickref.html#


## More with MicroPython on Raspberry Pi Pico

For more physical computing projects to try on your Raspberry Pi Pico, grab a copy of the new book, Get Started with MicroPython on Raspberry Pi Pico. 
As well as learning how to use Raspberry Pi Pico’s pins as inputs and outputs, you’ll build a simple game, measure temperatures, save and load data to 
your Pico’s file system, and even make a burglar alarm for your room .

[Get Started with MicroPython on Raspberry Pi Pico is available now from Raspberry Pi Press](https://magpi.cc/picobook).

Whats inside your GBE BOX
![Pico](https://user-images.githubusercontent.com/1426877/134377016-ab970d6b-3738-4b69-ad7e-c381f620e1c7.png)

