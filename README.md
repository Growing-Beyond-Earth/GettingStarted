# Thonny IDE with the Raspberry Pi Pico

In this first lesson, I will demonstrate how to use Thonny IDE and MicroPython on a Raspberry Pi Pico to do something simple with the Raspberry Pi Pico,

## Setup the environment
Let's begin by downloading and installing [Thonny Python IDE for beginners ](https://thonny.org/). 

Once Thonny is installed lets start by connecting the Raspberry Pi Pico to the computer via the USB cable. Start Thonny and Thonny should detect the Raspberry Pi Pico.

![Pico-Top-Plug-v2](https://user-images.githubusercontent.com/1426877/137755029-e5da0c8e-af08-48bd-8366-65ae495da883.png)

In the Thonny Tools menu, select "options", then "interpreter", and change the interpreter to the "MicroPython (Raspberry Pi Pico)" option. Also select the correct connection port for the device.
![Thonny-IDE-with-Raspberry-Pi-Pico-usb](https://user-images.githubusercontent.com/1426877/137755071-c7339229-fb2e-4d3b-bef7-818c0e9dab30.jpeg)

The Raspberry Pi Pico comes with MicroPython already flashed. This means that it is literally "plug and play"

## Documentation

You can find information about the Raspberry Pi Pico on its  [Pico web page](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html).  The Raspberry Pi Pico is well-equipped with all sorts of GPIO and communications capabilities.

## Experiment

## Writing a Script

Create a new script with File>New and paste in the following code:

```
print("Hello, World!")
```

Click the Green Play button to Run the code Thonny you will be prompted to save to your computer OR the pico. Select save to Pico and name the file lesson2.py

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

The time module provides functions for getting the current time and date, and for sleeping.

Python has two primitive loop commands:

-   while  loops
-   for  loops

we will us the While loop 
we set a variable n=0 start a While loop and print the thirteen-times table until you hit the stop button


Now lets say you want to stop at 13x37 how do we do that. 

```
from time import sleep

n = 0

while n < 38:
    print("13 x",n,"= ",13*n) # print the thirteen-times table
    n = n+1
    sleep(0.5)
```
now it will stop when n gets to 38

now we will add the ```else``` statement we can run a block of code once when the condition no longer is true:

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
We taken what we have leanred and made it a function we can call 

Functions are blocks of code that are referred to by name. Data can be passed into it to be operated on (i.e. the parameters) 
and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

Here is the same function passing in the times tabel we want "times" and the total of times "total" 
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


**NOTE: If you wish to run the code automatically whenever you power Raspberry Pi Pico then you have to name your code file as "main.py" while saving it.**

## MicroPython 1.7 Documnetation 

MicroPython 1.7 https://docs.micropython.org/en/latest/index.html https://docs.micropython.org/en/latest/rp2/quickref.html#



## More with MicroPython on Raspberry Pi Pico

For more physical computing projects to try on your Raspberry Pi Pico, grab a copy of the new book, Get Started with MicroPython on Raspberry Pi Pico. As well as learning how to use Raspberry Pi Pico’s pins as inputs and outputs, you’ll build a simple game, measure temperatures, save and load data to your Pico’s file system, and even make a burglar alarm for your room .

[Get Started with MicroPython on Raspberry Pi Pico is available now from Raspberry Pi Press](https://magpi.cc/picobook).
