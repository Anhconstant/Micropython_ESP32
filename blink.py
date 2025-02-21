from machine import Pin
import time
time.sleep(2)
def blinky_times(pin , times, f ):
    print("blink in "+str(times)+ " times , f = "+str(f))
    led = Pin(pin, Pin.OUT)
    t = 0
    while t<times:
        led.on()
        time.sleep_ms(100)
        led.off()
        time.sleep_ms(100)
        t=t+1
def blinky_forever(pin, f):
    t = int(1000/f)
    print("blink forever with "+ str(t) +" ms ")
    led = Pin(pin, Pin.OUT)
    while True:
        led.on()
        time.sleep_ms(t)
        led.off()
        time.sleep_ms(t)
    