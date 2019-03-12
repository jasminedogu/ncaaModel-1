from bs4 import BeautifulSoup
import requests
import csv
import sys
import mechanize
import cookielib
import math
from schedule import schedule
from mapping import mapTerms

# init team_data_dict
team_datas = []
team_fours = []
def main_page():
    page = requests.get('https://kenpom.com').content
    soup = BeautifulSoup(page, "html.parser")

    # get all rows
    trs = soup.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        if tds:
            team_dict = {}
            team_dict['rank']  = int(tds[0].string)
            school = tds[1].a.string
            team_dict['school'] = school
            team_dict['wins'] = int(tds[3].string.split('-')[0])
            team_dict['losses'] = int(tds[3].string.split('-')[1])

            team_dict['pyth'] = float(tds[4].string)

            team_dict['adj_o'] = float(tds[5].string)
            team_dict['adj_o_rank'] = int(tds[6].string)

            team_dict['adj_d'] = float(tds[7].string)
            team_dict['adj_d_rank'] = int(tds[8].string)

            team_dict['adj_t'] = float(tds[9].string)
            team_dict['adj_t_rank'] = int(tds[10].string)

            team_dict['luck'] = float(tds[11].string)
            team_dict['luck_rank'] = int(tds[12].string)

            team_dict['sos_pyth'] = float(tds[13].string)
            team_dict['sos_pyth_rank'] = int(tds[14].string)

            team_dict['sos_opp_o'] = float(tds[15].string)
            team_dict['sos_opp_o_rank'] = int(tds[16].string)

            team_dict['sos_opp_d'] = float(tds[17].string)
            team_dict['sos_opp_d_rank'] = int(tds[18].string)

            team_dict['ncsos_pyth'] = float(tds[19].string)
            team_dict['ncsos_pyth_rank'] = int(tds[20].string)
        
            team_datas.append(team_dict)

def fourFactor():
    login_data = {
    'email': 'Douglas.j.kim15@gmail.com',
    'password': 'Nadimissmall',
    }
    s = requests.Session()
    s.post('https://kenpom.com/handlers/login_handler.php', data=login_data)
    page = s.get('https://kenpom.com/stats.php').content
    print page
    soup = BeautifulSoup(page, "html.parser")

    # get all rows
    trs = soup.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        print len(tds)
        if tds:
            four_dict = {}
            school = tds[0].a.string
            four_dict['school'] = school
            four_dict['conf'] = tds[1].string
            team_fours.append(four_dict)



def comparison(data):
    spreadsheet = []
    for game in data:
        home = 0
        away = 0
        for team in team_datas:
            if game['home'] == team['school']:
                home = team
            elif game['away'] == team['school']:
                away = team
            elif away != 0 and home != 0:

                matchup = {}
                tempo = (home['adj_t'] + away['adj_t'])/2
                difference = home['pyth'] - away['pyth'] 
                sos = home['sos_pyth'] - away['sos_pyth']
                ncsos = home['ncsos_pyth'] - away['ncsos_pyth']

                # print "Home: " + home['school'] , " Away: " , away['school']
                # print "Adjem difference: " , difference
                # print "Adjem difference with tempo: " , difference * (tempo/100)
                # print "SOS difference: " , sos
                # print "SOS difference with tempo: " , sos * (tempo/100)
                # print "NCSOS difference: " , ncsos
                # print "NCSOS difference with tempo: " , ncsos * (tempo/100)

                dougValue = ((difference * (tempo/100)) + ((sos * (tempo/100)) * .35)) + 5
                #print "Dougs method: " , dougValue
                matchup['home'] = game['home']
                matchup['away'] = game['away']
                matchup['spread'] = game['spread']
                matchup['value'] = dougValue
                matchup['difference'] = dougValue - float(game['spread'])
                if matchup['difference'] > 0:
                    matchup['pick'] = matchup['home']
                else:
                    matchup['pick'] = matchup['away']
                if math.fabs(matchup['difference']) > 4:
                    matchup['level'] = 'high'
                elif math.fabs(matchup['difference']) > 2:
                    matchup['level'] = 'medium'
                else:
                    matchup['level'] = 'low'
                spreadsheet.append(matchup)
                break

    return spreadsheet


def release(data):
    with open('results.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, data[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data)

main_page()

data = schedule()
mapTerms(team_datas)
results = comparison(data)
release(results)
#fourFactor()
#print team_fours

with open('kenpom.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, team_datas[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(team_datas)