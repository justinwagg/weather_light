import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint
import time

# wget --content-disposition https://dl.dafont.com/dl/?f=pixel_operator
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
padding = -2
top = padding
bottom = height-padding

# font = ImageFont.load("helvB10.pil")
# font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Medium.ttf", 15)
font = ImageFont.truetype("/usr/share/fonts/truetype/lato/LiberationSans-Regular.ttf", 15)

# font = ImageFont.load_default()

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

x = 0
def draw(day, conditions, high, low, avehumidity):
	draw = ImageDraw.Draw(image)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((x, top), str(day), font=font, fill=255)
	draw.text((x, top+8), str(conditions) , font=font, fill=255)
	draw.text((x, top+16), "High:" + str(high) + " Low:" + str(low), font=font, fill=255)
	draw.text((x, top+25), "Humdity:" + str(avehumidity), font=font, fill=255)
	disp.image(image)
	disp.display()


def draw2(day, conditions, high, low, avehumidity, delta):
	if int(high) > 99:
		high = '*'
	if int(avehumidity) > 99:
		avehumidity = '*'
	draw = ImageDraw.Draw(image)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	disp.image(image)
	disp.display()
	font = ImageFont.truetype("/usr/share/fonts/truetype/lato/LiberationSans-Regular.ttf", 12)
	draw.text((x, top), str(day) + ": " + str(conditions) + "  (" + str(delta) + ")", font=font, fill=255)
	font = ImageFont.truetype("/usr/share/fonts/truetype/lato/LiberationSans-Regular.ttf", 15)
	# draw.text((x, top+8), str(conditions) , font=font, fill=255)
	draw.text((x, top+15), "Hi: " + str(high) + " Lo: " + str(low)+  " Hu: " + str(avehumidity), font=font, fill=255)
	# draw.text((x, top+25), "Humdity:" + str(avehumidity), font=font, fill=255)
	disp.image(image)
	disp.display()


def welcomeOLED():
	draw = ImageDraw.Draw(image)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((randint(0,50), randint(top,15)), "Welcome", font=font, fill=255)
	disp.image(image)
	disp.display()
	time.sleep(1)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((randint(0,50), randint(top,15)), "To", font=font, fill=255)
	disp.image(image)
	disp.display()
	time.sleep(1)	
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((randint(0,50), randint(top,15)), "Weather", font=font, fill=255)
	disp.image(image)
	disp.display()
	time.sleep(1)	
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((randint(0,50), randint(top,15)), "Friend", font=font, fill=255)	
	disp.image(image)
	disp.display()	
	time.sleep(1)	
	disp.image(Image.open('happycat_oled_32.ppm').convert('1'))
	disp.display()
	time.sleep(2)