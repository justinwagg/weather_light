color_dictionary = {
	'light_blue': { 
		'conditions': ['flurries', 'chanceflurries', 'snow', 'chancesnow'],
		'conditions_general' : 'Snow',
		'color': [240,248,255]
	},
	'dark_blue': {
		'conditions': ['rain', 'chancerain', 'tstorms', 'chancetstorms', 'sleet', 'chancesleet'],
		'conditions_general' : 'Wet',
		'color':[0, 0, 25]
	},
	'star': {
		'conditions': ['unknown'],
		'conditions_general' : 'Unknown',		
		'color':[0, 0, 0]
	},
	'white': {
		'conditions': ['cloudy', 'partlycloudy', 'mostlycloudy', 'fog'],
		'conditions_general' : 'Cloudy',		
		'color':[100, 100, 100]
	},
	'yellow': {
		'conditions': ['sunny', 'mostlysunny', 'partlysunny', 'clear'],
		'conditions_general' : 'Sunny',		
		'color':[255,255,0]
	},
	'orange': {
		'conditions': ['hazy'],
		'conditions_general' : 'Hazy',		
		'color':[255,69,0]
	}
}
