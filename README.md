# ncaaModel
Python prediction model for NCAA games

Scraper.py<br/>
  -Run this program to generate the csv, the other files are linked through here<br/>
  -Handles the website scraping, comparisons, and generates the csv that outputs on file run<br/>
  -Things to note:<br/>
      -The pick level by default is generated off of the home court advantage game value - spread. If you want to generate it for neutral court play you need to modify the variable "matchup['difference']"<br/>
      -This line: dougValue = ((difference * (tempo/100))+ ((sos * (tempo/100)) * .35)) + 5 does your score prediction. Modify that with the other variables passed into the list on scrape for better/different predictions.<br/>
<br/>
<br/>
Mapping.py<br/>
  -The teams from the lines xml do not always match with those from KenPom<br/>
  -This script adjusts the names so that they match. If you aren't getting a game, check this file and adjust the name here<br/>

<br/>
<br/>
Schedule.py
  -Parses the xml live lines tree to retrieve NCAA games for the night.
  
<br/>
<br/>
Final note, the spread always reflects the home team. -2 means that the home team is +2. Yea I know it's confusing...
  
  
  
