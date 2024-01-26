from machine import Pin, ADC, PWM  #importing PIN,ADC and PWM
import time #importing time   
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
# Defining motor pins

#OUT1  and OUT2
In1=Pin(7,Pin.OUT)  #IN1`
In2=Pin(6,Pin.OUT)  #IN2
EN_A=PWM(Pin(8))
EN_A.freq(1500)
Aspeed=20
EN_A.duty_u16(Aspeed)


#OUT3  and OUT4
In3=Pin(4,Pin.OUT)  #IN3
In4=Pin(3,Pin.OUT)  #IN4
EN_B=PWM(Pin(2))
Bspeed=0
EN_B.freq(1500)
EN_B.duty_u16(Bspeed)


def setBSpeed(newSpeed):
    if newSpeed < 65000 and newSpeed > 0:
        print('updating B duty cycle to ', newSpeed)
        EN_B.duty_u16(newSpeed)
    return newSpeed

def setASpeed(newSpeed):
    if newSpeed < 65000 and newSpeed > 0:
        print('updating A duty cycle to ', newSpeed)
        EN_A.duty_u16(newSpeed)
    return newSpeed
    
def move_left_forward():
    In1.high()
    In2.low()
    
def move_left_backward():
    In1.low()
    In2.high()


def move_right_forward():
    In3.low()
    In4.high()
    
def move_right_backward():
    In3.high()
    In4.low()
   
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()


    
