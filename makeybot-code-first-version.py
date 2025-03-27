
# Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import Servo
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins

traffic_light_refs = {"red": LED(3), "yellow": LED(4), "green": LED(17)}
eyes_refs = {"left-eye": [[PWMLED(27), .5], [PWMLED(22), .35], [PWMLED(23), 1]], "right-eye": [[PWMLED(10), .75], [PWMLED(9), .05], [PWMLED(24), .3]]}
arm_servo = Servo(14, min_pulse_width=.0008, max_pulse_width=.002)

def switch_to_stop(traffic_lights):
    for light, ref in zip(traffic_lights.keys(), traffic_lights.values()):
        if light == 'red':
            ref.on()
        else:
            ref.off()

def display_lights(traffic_lights, eyes_status):
    for light, ref in zip(traffic_lights.keys(), traffic_lights.values()):
        askForStatus = input(f"Do you want to turn on the {light} LED? [Y/N]: ")
        if askForStatus == "Y" or askForStatus == "y":
            ref.on()
        else:
            ref.off()
            
    for eye_name, eye in zip(eyes_status.keys(), eyes_status.values()):
        print(f"Setting pins for {eye_name}")
        for refs in eye:
            askForStatus = float(input("Pin (type a float from 0-1): "))
            pinRef = refs[0]
            refs[1] = askForStatus
            pinRef.value = askForStatus

def define_eyes_color(eyes_status):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes_status)
    for eye in eyes_status.values():
        for refs in eye:
            pinRef, statusRef = refs[0], refs[1]
            pinRef.value = statusRef
            
def get_robot_data():
    if debug_messages : print("Running get_robot_data function")
    left_eye, right_eye = eyes_refs
    switch_to_stop(traffic_light_refs)
    stop_light = {"red-light-status": 1, "yellow-light-status": 0, "green-light-status": 0}
    rfd = [stop_light, left_eye, right_eye]
    if debug_messages : print(rfd)
    if debug_messages: print("Returning get_robot_data function")
    return rfd

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    
    
    if debug_messages : print("Calling eyes_RGB function")
    define_eyes_color(eyes_refs)
    if debug_messages : print("Returned from eyes_RGB function")

main()
switch_to_stop(traffic_light_refs)
define_eyes_color(eyes_refs)
display_lights(traffic_light_refs, eyes_refs)
main()

arm_servo.min()
time.sleep(1)

arm_servo.mid()
time.sleep(1)

arm_servo.max()
time.sleep(1)


