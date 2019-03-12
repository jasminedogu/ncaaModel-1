def mapTerms(teams):
    for team in teams:
        if team['school'] == "Cal St. Northridge":
            team['school'] = "CS Northridge"
        elif team['school'] == "UNC Wilmington":
            team['school'] = "NC Wilmington"
        elif team['school'] == "UNC Greensboro":
            team['school'] = "NC Greensboro"
        elif team['school'] == "Southern Miss":
            team['school'] = "Southern Mississippi"
        elif team['school'] == "FIU":
            team['school'] = "Florida International"
        elif team['school'] == "Charlotte":
            team['school'] = "Charlotte University"
        elif team['school'] == "UTSA":
            team['school'] = "Texas San Antonio"
        elif team['school'] == "Little Rock":
            team['school'] = "Arkansas Little Rock"
        elif team['school'] == "Middle Tennessee":
            team['school'] = "Middle Tennessee State"
        elif team['school'] == "Portland":
            team['school'] = "Portland University"
        elif team['school'] == "UC Santa Barbara":
            team['school'] = "Cal Santa Barbara"
        elif team['school'] == "Washington":
            team['school'] = "Washington University"
        elif team['school'] == "Saint Mary's":
            team['school'] = "Saint Marys CA"
        elif team['school'] == "Fort Wayne":
            team['school'] = "IPFW"
        elif team['school'] == "Chattanooga":
            team['school'] = "Tennessee Chattanooga"
        elif team['school'] == "Idaho":
            team['school'] = "Idaho University"
        elif team['school'] == "St. Francis PA":
            team['school'] = "Saint Francis PA"
        elif team['school'] == "St. Francis NY":
            team['school'] = "Saint Francis NY"
        elif team['school'] == "VCU":
            team['school'] = "Virginia Commonwealth"
        elif team['school'] == "Detroit":
            team['school'] = "Detroit University"
        elif team['school'] == "Penn":
            team['school'] = "Pennsylvania"
        elif team['school'] == "Green Bay":
            team['school'] = "Wisconsin Green Bay" 
        elif team['school'] == "Milwaukee":
            team['school'] = "Wisconsin Milwaukee" 
        elif team['school'] == "Utah":
            team['school'] = "Utah University" 
        elif team['school'] == "Saint Peter's":
            team['school'] = "Saint Peters"
        elif "St." in team['school']:
            team['school'] = team['school'].replace("St.", "State")