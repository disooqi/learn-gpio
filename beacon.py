"""
an LED that is OFF will then turn ON gradually
and then gradually turn OFF like "breathing" or a beacon.
We achieve this by using Pulse-Width Modulation (or PWM).
All rights reserved to Mohamed Eldesouki
"""

__author__ = "Mohamed Eldesouki"
__date__ = "29 Dec, 2021"
__email__ = "pi@eldesouki.com"

import time
import RPi.GPIO as GPIO


class Beacon:
    LED_pin = 12
    pwm = None

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
        GPIO.setup(cls.LED_pin, GPIO.OUT)  # set LedPin to OUTPUT mode
        GPIO.output(cls.LED_pin, GPIO.LOW)  # make ledPin output LOW level to turn off LED

        cls.pwm = GPIO.PWM(cls.LED_pin, 500)  # set PWM Frequence to 500Hz
        cls.pwm.start(0)  # set initial Duty Cycle to 0

    @classmethod
    def deploy(cls):
        while True:
            for dc in range(0, 101, 1):  # make the led brighter
                cls.pwm.ChangeDutyCycle(dc)  # set dc value as the duty cycle
                time.sleep(0.01)
            time.sleep(1)
            for dc in range(100, -1, -1):  # make the led darker
                cls.pwm.ChangeDutyCycle(dc)  # set dc value as the duty cycle
                time.sleep(0.01)
            time.sleep(1)

    @classmethod
    def destroy(cls):
        cls.pwm.stop()  # stop PWM
        GPIO.cleanup()  # Release all GPIO


if __name__ == '__main__':
    print('Program is starting ... ')
    Beacon.initialize()
    try:
        Beacon.deploy()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        Beacon.destroy()
