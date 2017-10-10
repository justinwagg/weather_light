# Weather Light

An led light that indicates tomorrows conditions relative to today, and gives some basic weather stats on an OLED. 

## To Do:

- Add error handling on the api request
- Figure out how to transition light from color to color
- Control the OLED
- Control the LED

## Structure:

```
|-- weather_light
	|-- get_weather.py - responsible for hitting Wunderground API
	|-- storage.py - responsible for holding painfully large variables
	|-- oled.py - responsible for controlling the display
	|-- lighting.py - responsible for controlling the LED
	|-- main.py - responsible for coordinating the show
```