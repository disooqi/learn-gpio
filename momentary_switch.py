"""
An implementation to a momentary switch
"""
__author__ = "Mohamed Eldesouki"
__date__ = "27 Dec, 2021"
__email__ = "pi@eldesouki.com"

import time
import RPi.GPIO as GPIO


led_pin = 11
button_pin = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    # current state of the button
    button_current_state = GPIO.HIGH  # HIGH means it is released

    # I know; 0 means ON, 1 means OFF (for the button)
    led_states = ['\033[32mled turned ON\033[0m', '\033[31mled turned OFF\033[0m']
    print(led_states[button_current_state])

    while True:
        time.sleep(0.1)
        if button_current_state != GPIO.input(button_pin):
            GPIO.output(led_pin, button_current_state)
            button_current_state = GPIO.input(button_pin)
            print(led_states[button_current_state])


def destroy():
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    print('System ready')
    print('Please press the button')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
