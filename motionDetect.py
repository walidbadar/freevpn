import RPi.GPIO as GPIO
# import OPi.GPIO as GPIO
import time, datetime, threading

# import serial
#
# ser = serial.Serial("COM4", baudrate=115200, timeout=0.001)

# Variable for the GPIO pin number
solenoidLock = 3
LED_pin = 5
doorSensor = 7
motionSensor = 11

# Orange Pi Zero Board
# GPIO.setboard(GPIO.ZERO)

# Set up the GPIO pin for I/O
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setup(solenoidLock, GPIO.OUT, initial=GPIO.LOW)  # solenoidLock output pin
GPIO.setup(LED_pin, GPIO.OUT, initial=GPIO.LOW)  # LED output pin
GPIO.setup(doorSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Read output from door sensor
GPIO.setup(motionSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Read output from PIR motion sensor

# Adjustable Parameters
brightness = 0
brightnessDelay = 0.005
fadeOnCount = 0
fadeOffCount = 0
motionCount = 0
motionSenseDelay = 10000  # milliseconds
sleepTime = 60  # seconds
sixHoursWaitTimer = ''

# Creates software PWM on LED_pin running at 50Hz
pwm = GPIO.PWM(LED_pin, 100)
pwm.start(brightness)


def fadeOn():
    for brightness in range(0, 101, 1):
        pwm.ChangeDutyCycle(brightness)
        time.sleep(brightnessDelay)
    print("fadeOn Brightness")


def fadeOff():
    for brightness in range(100, -1, -1):
        pwm.ChangeDutyCycle(brightness)
        time.sleep(brightnessDelay)
    print("fadeOff Brightness")


def sixHoursWait():
    global motionCount
    print("six Hours Wait Ended")
    print(datetime.datetime.now())

    motionCount = 0
    GPIO.add_event_detect(motionSensor, GPIO.FALLING, callback=motionDetection, bouncetime=motionSenseDelay)


# This function will be used to Fade ON and Fade Off the LED
def motionDetection(motion=None):
    global motionCount, sixHoursWaitTimer

    GPIO.remove_event_detect(motionSensor)
    motionCount = motionCount + 1

    print(datetime.datetime.now())
    if motionCount <= 3:
        print(motionCount)

        for brightness in range(0, 101, 1):
            pwm.ChangeDutyCycle(brightness)
            time.sleep(brightnessDelay)

        for brightness in range(100, -1, -1):
            pwm.ChangeDutyCycle(brightness)
            time.sleep(brightnessDelay)

    GPIO.add_event_detect(motionSensor, GPIO.FALLING, callback=motionDetection, bouncetime=motionSenseDelay)
    print("fadeOn and fadeOff Brightness")

    if motionCount == 3:
        print("six Hours Wait Started")
        print(datetime.datetime.now())

        GPIO.remove_event_detect(motionSensor)
        sixHoursWaitTimer = threading.Timer(sleepTime, sixHoursWait)
        sixHoursWaitTimer.start()


# Run Continuously in loop
print("Program Started")
print(datetime.datetime.now())


def loop():
    global motionCount, sixHoursWaitTimer

    GPIO.add_event_detect(motionSensor, GPIO.FALLING, callback=motionDetection, bouncetime=motionSenseDelay)
    while True:
        if GPIO.input(doorSensor):
            GPIO.remove_event_detect(motionSensor)

            fadeOn()
            while GPIO.input(doorSensor):
                # print("Door is opened", GPIO.input(doorSensor))
                GPIO.output(LED_pin, 1)
            fadeOff()

            if sixHoursWaitTimer != '':
                sixHoursWaitTimer.cancel()
            motionCount = 0
            GPIO.add_event_detect(motionSensor, GPIO.FALLING, callback=motionDetection, bouncetime=motionSenseDelay)
        pass  # Don't do anything, sit forever


if __name__ == '__main__':
        loop()
