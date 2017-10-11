from datetime import datetime, timedelta
from get_weather import current, forecast
from storage import color_dictionary

#https://www.amazon.com/Light-Accents-Table-Natural-Wooden/dp/B01MYWYM0X/ref=sr_1_2?s=hi&ie=UTF8&qid=1507602398&sr=1-2&keywords=frosted+glass+sphere

#set update time to be on the hour every hour
current_time = datetime.now()
prior_read = current_time - timedelta(hours = 1)


if current_time.hour != prior_read.hour:
	city, observation_time, temperature_string, feelslike_string, relative_humidity = current()
	today_conditions, today_icon, today_high, today_low, today_avehumidity, tomorrow_conditions, tomorrow_icon, tomorrow_high, tomorrow_low, tomorrow_avehumidity = forecast()
	prior_read = current_time

	#one variable to moderate color/intensity will be the temperature delta between the two days
	high_temp_delta = int(tomorrow_high) - int(today_high)

	for x in color_dictionary:
		if tomorrow_icon in (color_dictionary[x]['conditions']):
			tomorrow_color = color_dictionary[x]['color']
			break
		else:
			tomorrow_color = 'null'

	print('Tomorrows condition will be {}, a color of {}. The high delta will be {}.'.format(tomorrow_icon, tomorrow_color, high_temp_delta))



