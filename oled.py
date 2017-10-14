import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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

font = ImageFont.load_default()

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


