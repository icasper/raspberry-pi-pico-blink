from machine import Pin
from time import sleep_ms

led = Pin(25, Pin.OUT)

while True:
    led.value(0)
    sleep_ms(128)
    led.value(1)
    sleep_ms(128)
