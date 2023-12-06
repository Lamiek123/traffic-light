from sound import buzzer
from servo import servo
from Numbers import Segments

buzzer = PWM(Pin(9))
servoe = Servo(pin=12)
Sledred = Pin(15, Pin.OUT)
Sledgreen = Pin(15, Pin.OUT)
Sledyellow = Pin(15, Pin.OUT)
Nledred = Pin(15, Pin.OUT)
Nledgreen = Pin(15, Pin.OUT)
Nledyellow = Pin(15, Pin.OUT)
buttonemergency = Pin(10, Pin.IN)
trainbutton = Pin(11, Pin.IN)
trainled = pin(12, pin.IN)
 
 
while True:
    if buttonemergency.value():
        Sledred.toggle()
        Sledgreen.toggle()
        Sledyellow.toggle()
        Nledred.toggle()
        Nledgreen.toggle()
        Nledyellow.toggle()
        trainled.toggle()
        utime.sleep(1)