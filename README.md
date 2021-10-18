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

Click the Green Play button to Run the code Thonny will ask you where do you want to save it 

<img width="1068" alt="SavePico" src="https://user-images.githubusercontent.com/1426877/137758143-fb010874-a2ba-4475-b0c4-9c2bd010cc88.png">


**NOTE: If you wish to run the code automatically whenever you power Raspberry Pi Pico then you have to name your code file as "main.py" while saving it.**

## More with MicroPython on Raspberry Pi Pico

For more physical computing projects to try on your Raspberry Pi Pico, grab a copy of the new book, Get Started with MicroPython on Raspberry Pi Pico. As well as learning how to use Raspberry Pi Pico’s pins as inputs and outputs, you’ll build a simple game, measure temperatures, save and load data to your Pico’s file system, and even make a burglar alarm for your room .

[Get Started with MicroPython on Raspberry Pi Pico is available now from Raspberry Pi Press](https://magpi.cc/picobook).
