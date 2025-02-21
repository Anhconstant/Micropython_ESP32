from machine import Pin
import time
time.sleep(2)
ver = "1.0"
print("main in ver "+ ver)
print("start main")
led = Pin(15,Pin.OUT)

while True:
    led.value(not(led.value()))
    time.sleep_ms(100)
    