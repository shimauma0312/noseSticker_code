# coding: utf-8

import time
import RPi.GPIO as GPIO
import spidev
import pygame.mixer

#300 ~ 1000
threshold = 900 

pygame.mixer.init()
#/home/pi/data/hoge.mp3
#/home/pi/などが好ましいんじゃ
#fileパス
pygame.mixer.music.load("mp3") 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz=1000000

spi.bits_per_word=8

dummy = 0xff
start = 0x47
sgl = 0x20

ch0 = 0x00

msbf = 0x08

def measure(ch):
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    val = ((ad[0] & 0x03) << 8) + ad[1]
    return val

try:
    while 1:
        time.sleep(0.237)

        GPIO.output(22,True)
        time.sleep(0.005)

        ch0_val = measure(ch0)
        Val = 1023 - ch0_val
        time.sleep(0.002)
        GPIO.output(22,False)
        
        GPIO.output(17,True)
        time.sleep(0.008)
        GPIO.output(17,False)

        print Val

        #if Val > threshold:
           # pygame.mixer.music.play(0)

except KeyboardInterrupt:
    pass

pygame.mixer.music.stop()
spi.close()
