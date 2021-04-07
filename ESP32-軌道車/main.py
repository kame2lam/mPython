from machine import Pin

motor=[Pin(0,Pin.OUT),
       Pin(2,Pin.OUT),
       Pin(13,Pin.OUT),
       Pin(15,Pin.OUT)]

def forward():
    motor[0].value(1)
    motor[1].value(0)
    motor[2].value(1)
    motor[3].value(0)
    
def backward():
    motor[0].value(0)
    motor[1].value(1)
    motor[2].value(0)
    motor[3].value(1)

def stop():
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(0)
    
def left():
    motor[0].value(0)
    motor[1].value(0)
    motor[2].value(1)
    motor[3].value(0)

def right():
    motor[0].value(1)
    motor[1].value(0)
    motor[2].value(0)
    motor[3].value(0)

while True:
    P12=Pin(12, Pin.IN).value()
    P14=Pin(14, Pin.IN).value()
    value=P12*2+P14
    print(value)
    if value==0:
        forward()
    if value==3:
        backward()
    if value==1:
        left()
    if value==2:
        right()
  