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
    # current state of the LED
    led_current_state = GPIO.LOW  # False means it is OFF

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(cls.led_pin, GPIO.OUT)
        GPIO.setup(cls.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @classmethod
    def toggle_LED(cls):
        cls.led_current_state = not cls.led_current_state
        GPIO.output(cls.led_pin, cls.led_current_state)

    @classmethod
    def deploy(cls):
        # I know; 0 means ON, 1 means OFF (for the button)
        led_states = ['\033[31mLED turned OFF\033[0m', '\033[32mLED turned ON\033[0m']
        print("\033[34mLED is OFF, press the button to switch it ON\033[0m")
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
                cls.toggle_LED()
                print(led_states[cls.led_current_state], count)
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
    try:
        ToggleSwitch.deploy()
    except KeyboardInterrupt:
        ToggleSwitch.destroy()
