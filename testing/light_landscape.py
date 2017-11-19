import time
import datetime
from neopixel import *
import random


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
		brightness = 25
	else:
		brightness = 100
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
	strip.setBrightness(brightness())
	for j in range(256*iterations):
		# strip.setBrightness(brightness()-translate(j, 10, 256*iterations, 0, brightness()))
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
	down()
		

def rgb(r, g, b):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, neopixel.Color(r,g,b))
	strip.show()

def rgb2(r, g, b):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(r,g,b))
		strip.show()
		time.sleep(3)		

def up(r, g, b):
	for i in range(brightness()):
		for j in range(strip.numPixels()):
			strip.setPixelColor(j, Color(r, g, b))
		strip.setBrightness(i)
		strip.show()
		time.sleep(1/1000.0)	




strip.setPixelColor(2, Color(0,100,0))
strip.setPixelColor(12, Color(0,100,0))
strip.show()

ground_color = [4, 5, 6, 7, 8, 9, 10]
sky_color = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3]
def ground(r, g, b):
	for i in range(len(ground_color)):
		strip.setPixelColor(ground_color[i], Color(r,g,b))
		print(ground_color[i])
	strip.show()

def sky(r, g, b):
	for i in range(len(sky_color)):
		strip.setPixelColor(sky_color[i], Color(r,g,b))
		print(sky_color[i])
	strip.show()


def sky(iterations = 50):
	for j in range(iterations):
		for i in range(random.randint(1,len(sky_color))):
			strip.setPixelColor(sky_color[random.randint(0,len(sky_color)-1)], Color(0,0,random.randint(25,50)))
		strip.show()
		time.sleep(random.randint(80,100)/1000.0)


from colour import Color as ccc

# orange = rgb(255,69,0)
# blue = rgb(65,105,225)

red = Color(rgb=(1.0, 0.0, 0.0))
green = Color(rgb=(0.0, 1.0, 0.0))

orange = Color(rgb=(255.0/1000.0, 69.0/1000.0, 0.0/1000.0))
blue_light = Color(rgb=(65.0/1000.0, 105.0/1000.0, 225.0/1000.0))
blue = Color(rgb=(0/1000.0, 0/1000.0, 225/1000.0))

rgb(0,0,255)
color_list = list(blue_light.range_to(blue,100))
#color change
for i in range(len(color_list)):
	r = int(round(color_list[i].red * 100))
	g = int(round(color_list[i].green * 100))
	b = int(round(color_list[i].blue * 100))
	for j in range(strip.numPixels()):
		strip.setPixelColor(j, neopixel.Color(r, g, b))
	strip.show()
	time.sleep(50/1000.0)


# color1 = Color(rgb=(255.0/1000.0, 69.0/1000.0, 0.0/1000.0))
# color2 = Color(rgb=(255.0/1000.0, 69.0/1000.0, 0.0/1000.0))
# color2.saturation = .75

color1 = Color(rgb=(255.0/1000.0, 69.0/1000.0, 0.0/1000.0))
color2 = Color(rgb=(255.0/1000.0, 69.0/1000.0, 0.0/1000.0))
color2.saturation = .75

def saturation_glow():
	direction = True
	for i in range(0,10):
		if direction:
			color_list = list(color1.range_to(color2,10))
		else:
			color_list = list(color2.range_to(color1,10))
		for i in range(len(color_list)):
			r = int(round(color_list[i].red * 100))
			g = int(round(color_list[i].green * 100))
			b = int(round(color_list[i].blue * 100))
			for j in range(strip.numPixels()):
				strip.setPixelColor(j, neopixel.Color(r, g, b))
			strip.show()
			time.sleep(40/1000.0)
		direction = not direction
