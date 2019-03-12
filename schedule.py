import requests
import xml.etree.ElementTree as ET




def schedule():
	table = []
	
	response = requests.get('http://lines.bookmaker.eu/')
	
	root = ET.fromstring(response.content)
	
	#for child in root.iter('league'):
			#for game in child.iterfind('league[@IdLeague="4"]'):
	games = root.find("./Leagues/league[@IdLeague='4']")
	for game in games.findall('game'):
		gm = {}
		home = game.get("htm")
		away = game.get("vtm")
		spread = -1000
		for line in game.iter('line'):
			spread = line.get("vsprdt")

		gm['home'] = home
		gm['away'] = away
		gm['spread'] = spread

		table.append(gm)

	return table