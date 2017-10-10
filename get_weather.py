import urllib2
import json

def current():
	# get current conditions
	current_conditions = urllib2.urlopen('http://api.wunderground.com/api/47df74743fe5842b/conditions/q/NY/NewYork.json')

	# parse current conditions
	current_conditions_string = current_conditions.read()
	current_conditions_parsed = json.loads(current_conditions_string)

	# store current condition details
	city = current_conditions_parsed['current_observation']['display_location']['full']
	observation_time = current_conditions_parsed['current_observation']['observation_time']
	temperature_string = current_conditions_parsed['current_observation']['temperature_string']
	feelslike_string = current_conditions_parsed['current_observation']['feelslike_string']
	relative_humidity = current_conditions_parsed['current_observation']['relative_humidity']

	return(city, observation_time, temperature_string, feelslike_string, relative_humidity)

def forecast():
	# get forecast conditions
	# forecast_parsed['forecast']['simpleforecast'] contains a 4 day simple outlook
	forecast = urllib2.urlopen('http://api.wunderground.com/api/47df74743fe5842b/forecast/q/NY/NewYork.json')

	# parse current conditions
	forecast_string = forecast.read()
	forecast_parsed = json.loads(forecast_string)

	# results come down in nested json - I'm not sure if "today" will always be period 1
	# and whether tomorrow will always be period 2, so I'm getting the index number
	# so I can look up where period 1 and 2 actually are
	# *making the assumption that at least the periods will be consistent over time*
	periods = []
	for i in range(0, len(forecast_parsed['forecast']['simpleforecast']['forecastday'])):
		periods.append(forecast_parsed['forecast']['simpleforecast']['forecastday'][i]['period'])

	today_period_index = periods.index(1)
	tomorrow_period_index = periods.index(2)

	# grab todays high high/low temp and avg. humidity
	today_conditions = forecast_parsed['forecast']['simpleforecast']['forecastday'][today_period_index]['conditions']
	today_icon = forecast_parsed['forecast']['simpleforecast']['forecastday'][today_period_index]['icon']
	today_high = forecast_parsed['forecast']['simpleforecast']['forecastday'][today_period_index]['high']['fahrenheit']
	today_low = forecast_parsed['forecast']['simpleforecast']['forecastday'][today_period_index]['low']['fahrenheit']
	today_avehumidity = forecast_parsed['forecast']['simpleforecast']['forecastday'][today_period_index]['avehumidity']

	# grab tomorrows high high/low temp and avg. humidity
	tomorrow_conditions = forecast_parsed['forecast']['simpleforecast']['forecastday'][tomorrow_period_index]['conditions']
	tomorrow_icon = forecast_parsed['forecast']['simpleforecast']['forecastday'][tomorrow_period_index]['icon']
	tomorrow_high = forecast_parsed['forecast']['simpleforecast']['forecastday'][tomorrow_period_index]['high']['fahrenheit']
	tomorrow_low = forecast_parsed['forecast']['simpleforecast']['forecastday'][tomorrow_period_index]['low']['fahrenheit']
	tomorrow_avehumidity = forecast_parsed['forecast']['simpleforecast']['forecastday'][tomorrow_period_index]['avehumidity']

	return(today_conditions, today_icon, today_high, today_low, today_avehumidity, tomorrow_conditions, tomorrow_icon, tomorrow_high, tomorrow_low, tomorrow_avehumidity)