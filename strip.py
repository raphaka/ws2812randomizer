from rpi_ws281x import *
import random

# LED strip configuration:
LED_COUNT      = 60
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0

#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#strip.begin()

iterations = 3
flash_period = 0.1
shelf_start = [0,20,40]  #erste Led im Fach
shelf_width = 20

#COLORS
roll_color_foreground = Color(255, 255, 255)
roll_color_background = Color(0, 0, 0)
choice_color_foreground = Color(0, 255, 0)
choice_color_background = Color(0, 0, 0)

def randomize():
    #set all leds to choice background color
    # for i in range(0,LED_COUNT):
        # strip.setPixelColor(i, choice_color_foreground)
    #choose random shelf
    hat = random.randint(0,len(shelf_start)-1)
    led_start = shelf_start[hat]
    led_end = led_start + shelf_width
    for i in range(led_start,led_end):
        print("pixel " + str(i))
        # strip.setPixelColor(i, choice_color_foreground)

def roll():
    for g in range(0,iterations):
        #flash each shelf in foregground color for short time
        for h in range(0,len(shelf_start)):
            led_start = shelf_start[h]
            led_end = led_start + shelf_width
            for i in range(led_start,led_end):
                print("pixel " + str(i))
                # strip.setPixelColor(i, roll_color_foreground)
            # time.sleep(flash_period)
            # for i in range(led_start,led_end):
            #     print("pixel " + str(i))
            #     strip.setPixelColor(i, roll_color_background)
            print(" ")

if __name__ == '__main__':
    roll()
    randomize()
