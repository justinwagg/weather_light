import time
import datetime
from lighting import *

# from datetime import datetime, timedelta
# import datetime
from oled import draw2, welcomeOLED
from multiprocessing import Process
# brightness()
p1 = Process(target=welcome, args=[strip])
p1.start()
p2 = Process(target=welcomeOLED)
p2.start()

from get_weather import current, forecast
from storage import color_dictionary


current_time = datetime.datetime.now()
prior_read = current_time - datetime.timedelta(hours = 1)	

while True:
	#set update time to be on the hour every hour
	current_time = datetime.datetime.now()
	if current_time.hour != prior_read.hour:
		city, observation_time, temperature_string, feelslike_string, relative_humidity = current()
		today_day, today_conditions, today_icon, today_high, today_low, today_avehumidity, tomorrow_day, tomorrow_conditions, tomorrow_icon, tomorrow_high, tomorrow_low, tomorrow_avehumidity = forecast()
		prior_read = current_time

		#one variable to moderate color/intensity will be the temperature delta between the two days
		high_temp_delta = int(tomorrow_high) - int(today_high)

		for x in color_dictionary:
			if tomorrow_icon in (color_dictionary[x]['conditions']):
				tomorrow_color = color_dictionary[x]['color']
				tomorrow_general_condition = color_dictionary[x]['conditions_general']
				break
			else:
				tomorrow_color = [255, 0, 0]
				tomorrow_general_condition = 'unknown'

		for x in color_dictionary:			
			if today_icon in (color_dictionary[x]['conditions']):
				today_color = color_dictionary[x]['color']
				today_general_condition = color_dictionary[x]['conditions_general']
			else:
				today_color = [255, 0, 0]
				today_general_condition = 'unknown'

		print('Ok - Got Weather, All Clear')
		
		while p1.is_alive() or p2.is_alive():
			time.sleep(0.25)

		if current_time.hour < 12:
			color = today_color
			day = today_day
			general_condition = today_general_condition
			high = today_high
			low = today_low
			avehumidity = today_avehumidity
			icon = today_icon
			delta = '*'
		else:
			color = tomorrow_color
			day = tomorrow_day
			general_condition = tomorrow_general_condition
			high = tomorrow_high
			low = tomorrow_low
			avehumidity = tomorrow_avehumidity
			icon = tomorrow_icon
			delta = high_temp_delta	

		brightness()
		up(color[0], color[1], color[2])
		draw2(day, general_condition, high, low, avehumidity, delta)
		print('Tomorrows condition will be {}, a color of {}. The high delta will be {}. Icon = {}'.format(general_condition, color, high_temp_delta, icon))
