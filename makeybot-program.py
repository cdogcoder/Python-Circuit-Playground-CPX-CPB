# Importing necessary libraries 
# gpiozero for manipulating the LEDs through the LED object
# time for inserting time pauses throughout the program

from gpiozero import LED
import time

# Initialize a dictionary 'traffic_lights', which contains the names of
# the LEDs as dictionary keys and lists containing the light's status
# and reference number on the Raspberry Pi 5 (in accordance with Broadcom
# references) as dictionary  values

traffic_lights = {'red_LED': [0,3], 'yellow_LED': [0,27], 'green_LED': [0,13]}

# Define a function 'display_light', which takes an argument 'lights' and
# iterates through it ('lights' is taken to be an iterable object, more
# specifically a dictionary). For each value in 'lights', we obtain the 
# light status and reference of the current LED and set its light status
# to be the opposite of what it currently is. For example, if the light
# status of a particular LED is on (1), we will turn it off (0) and reflect
# that change visually via the reference method.

def display_light(lights):
    for status in lights.values():
        lightStatus = status[0]
        light = LED(status[1])
        if lightStatus == 0:
            status[0] = 1
            light.on()
        else:
            status[0] = 0
            light.off()
        time.sleep(1)
    
# Define a function 'main' to run all of our program's primary code.
# Currently, the function only runs the 'display_light' function, passing
# to it the 'traffic_lights' dictionary as an argument. This will change
# later on.
    
def main():
    display_light(traffic_lights)											
    
# Call function 'main'
            
main()
