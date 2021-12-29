import time
import RPi.GPIO as GPIO


ledPin = 11    # define ledPin


def setup():
    # pin serial number based on CPU of BCM chip.
    # GPIO.setmode(GPIO.BCM)

    # use PHYSICAL GPIO Numbering
    GPIO.setmode(GPIO.BOARD)

    # set the ledPin to OUTPUT mode
    GPIO.setup(ledPin, GPIO.OUT)

    # make ledPin output LOW level
    GPIO.output(ledPin, GPIO.LOW)
    print(f'Using pin {ledPin}')


def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
        print('\033[32mled turned on\033[0m')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
        print('\033[31mled turned off\033[0m')
        time.sleep(1)                   # Wait for 1 second


def destroy():
    """Release all GPIO"""
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

