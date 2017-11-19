import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


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
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
