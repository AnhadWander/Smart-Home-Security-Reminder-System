from machine import Pin, SPI
import time
from time import sleep
from ili9341 import Display, color565
import os
from wavePlayer import wavePlayer
from machine import Pin, SPI

spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
display.clear()

mag_switch = Pin(0, Pin.IN)
led = Pin('LED', Pin.OUT)

ldr = machine.ADC(27)
ldr_value = ldr.read_u16()

player = wavePlayer()
    
while True:
    ldr_value = ldr.read_u16()
    print(mag_switch.value())
    print(ldr_value)
    if ldr_value > 400 and mag_switch.value() == 0:
        display.clear(color565(255, 255, 255))
        display.draw_text8x8(0, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(20, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(40, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(60, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(80, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(100, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(120, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(140, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(160, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(180, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(200, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.draw_text8x8(220, 0, "ALERT....ALERT....ALERT....ALERT...ALERT", color565(0, 0, 0), rotate=90, background=color565(255,255,255))
        display.fill_polygon(3, 90, 160, 140, color565(0,0,0))
        display.fill_polygon(3, 90, 160, 120, color565(0, 255, 0),)
        display.fill_rectangle(85,150,82,20, color565(0,0,0))
        display.fill_circle(55,160,12, color565(0,0,0))
        while ldr_value > 400 and mag_switch.value() == 0:
            player.play("signal_alert_short.wav")
            
    else: 
        display.clear()

    time.sleep(0.2)


