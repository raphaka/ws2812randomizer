#from rpi_ws281x import *
import random

# LED strip configuration:
LED_COUNT      = 30
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0

#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#strip.begin()

iterations = 3
shelf_start = [0,10,20]  #erste Led im Fach
shelf_width = 10

def randomize():
    hat = random.randint(0,len(shelf_start)-1)
    led_start = shelf_start[hat]
    led_end = led_start + shelf_width
    for i in range(led_start,led_end):
        print("pixel " + str(i))
        #strip.setPixelColor(i, color)

def roll():
    for g in range(0,iterations):
        for h in range(0,len(shelf_start)):
            led_start = shelf_start[h]
            led_end = led_start + shelf_width
            for i in range(led_start,led_end):
                print("pixel " + str(i))
            print(" ")

if __name__ == '__main__':
    roll()
    randomize()
