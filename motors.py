# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time #

# Set GPIO Modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 9
pinMotorABackwards = 10
pinMotorBForwards = 7
pinMotorBBackwards = 8

pinOnOff = 23


# Set the GPIO Pin mode
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)

GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)

GPIO.setup(pinOnOff, GPIO.IN)

def forwardsA():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)

def forwardsB():
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)   

def backwardsA():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)

def backwardsB():
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)   


def stopA():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)

def stopB():
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)    

def stopMotors():
    stopA()
    stopB()

def forward(t):
    forwardsA()
    forwardsB()
    time.sleep(t)
    stopMotors()

def backward(t):
    backwardsA()
    backwardsB()
    time.sleep(t)
    stopMotors()

def left(t):
    backwardsA()
    forwardsB()
    time.sleep(t)
    stopMotors()

def right(t):
    backwardsB()
    forwardsA()    
    time.sleep(t)
    stopMotors()
    
def isOn():
    GPIO.input(pinOnOff)


forward(1)

