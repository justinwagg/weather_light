import time
import datetime
from neopixel import *



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

#8am - 8pm - 100
#else 25



# orange = rgb(255,69,0)
# blue = rgb(65,105,225)
# light blue = rgb(240,248,255)
# pink = rgb(220,20,60)
def brightness():
	if datetime.datetime.now().hour >= 20 or datetime.datetime.now().hour <= 8:
		brightness = 15
		strip.setBrightness(brightness)
	else:
		brightness = 100
		strip.setBrightness(brightness)
	return brightness

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return int(round(rightMin + (valueScaled * rightSpan)))		

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)


def down():
	for i in reversed(range(brightness())):
		strip.setBrightness(i)
		time.sleep(5/1000.0)
		strip.show()

def welcome(strip, wait_ms=1, iterations=5):
	for j in range(256*iterations):
		# strip.setBrightness(brightness()-translate(j, 10, 256*iterations, 0, brightness()))
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
	down()
		

def rgb(r, g, b):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(r,g,b))
	strip.show()

		

def up(r, g, b):
	for i in range(brightness()):
		for j in range(strip.numPixels()):
			strip.setPixelColor(j, Color(r, g, b))
		strip.setBrightness(i)
		strip.show()
		time.sleep(1/1000.0)	

