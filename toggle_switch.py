"""
An implementation to a toggle switch
"""
__author__ = "Mohamed Eldesouki"
__date__ = "28 Dec, 2021"
__email__ = "pi@eldesouki.com"


import time
import RPi.GPIO as GPIO


class ToggleSwitch:
    led_pin = 11
    button_pin = 12

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(cls.led_pin, GPIO.OUT)
        GPIO.setup(cls.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @classmethod
    def deploy(cls):
        # current state of the LED
        led_current_state = GPIO.LOW  # False means it is OFF

        # I know; 0 means ON, 1 means OFF (for the button)
        led_states = ['\033[31mled turned OFF\033[0m', '\033[32mled turned ON\033[0m']
        print(led_states[led_current_state])
        still_pressed = False
        count = 1
        while True:
            time.sleep(0.01)
            if GPIO.input(cls.button_pin) == GPIO.LOW:
                if still_pressed:
                    # this is added to solve the bounce problem
                    # to eliminate the impact of buffeting.
                    time.sleep(0.05)
                    count += 1
                    continue
                led_current_state = not led_current_state
                GPIO.output(cls.led_pin, led_current_state)
                print(led_states[led_current_state], count)
                count = 0
                still_pressed = True
                #
            else:
                still_pressed = False

    @staticmethod
    def destroy():
        # GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    ToggleSwitch.initialize()

    print('System ready')
    print('Please press the button')
    try:
        ToggleSwitch.deploy()
    except KeyboardInterrupt:
        ToggleSwitch.destroy()
