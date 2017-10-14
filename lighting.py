import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


# orange = rgb(255,69,0)
# blue = rgb(65,105,225)
# light blue = rgb(240,248,255)
# pink = rgb(220,20,60)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return int(round(rightMin + (valueScaled * rightSpan)))		


def rgb(r, g, b):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(r,g,b))
	strip.show()

def welcome(strip, wait_ms=2, iterations=5):
	for j in range(256*iterations):
		strip.setBrightness(255-translate(j, 0, 256*iterations, 0, 255))
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)


up(255,69,0)	



up
down()
def down():
	for i in reversed(range(255)):

		strip.show()
		time.sleep(5/1000.0)

def up(r, g, b):
	for i in range(255):
		for j in range(strip.numPixels()):
			strip.setPixelColor(j, Color(r, g, b))
		strip.setBrightness(i)
		strip.show()
		time.sleep(1/1000.0)	

