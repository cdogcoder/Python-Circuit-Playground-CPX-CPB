import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

bobs_button_B = digitalio.DigitalInOut(board.BUTTON_B)
bobs_button_B.direction = digitalio.Direction.INPUT
bobs_button_B.pull = digitalio.Pull.DOWN

def main():
    print("Hello")
    print(dir(board))
    print(dir(digitalio))
    print(dir(digitalio.DigitalInOut))
    print(dir(digitalio.Direction))
    print(dir(digitalio.Pull))
    while True:
        led.value = bobs_button_B.value
        print(bobs_button_B.value)
        time.sleep(.5)


main()

