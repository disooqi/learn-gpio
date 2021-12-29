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
    def toggle_LED(cls, channel):
        led_states = ['\033[31mLED turned OFF\033[0m', '\033[32mLED turned ON\033[0m']
        cls.led_current_state = not cls.led_current_state
        GPIO.output(cls.led_pin, cls.led_current_state)
        print(led_states[cls.led_current_state], '- switch at channel', channel)

    @classmethod
    def deploy(cls):
        print("\033[34mLED is OFF, press the button to switch it ON\033[0m")
        GPIO.add_event_detect(cls.button_pin, GPIO.FALLING, callback=cls.toggle_LED, bouncetime=300)
        while True:
            pass

    @classmethod
    def destroy(cls):
        GPIO.output(cls.led_pin, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    ToggleSwitch.initialize()
    print('\033[44m\033[30m  System is ready  \033[0m')
    try:
        ToggleSwitch.deploy()
    except KeyboardInterrupt:
        ToggleSwitch.destroy()
