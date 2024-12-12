from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import schedule
import requests
from notifier import send
from alerts import fetch_data

# class Buoy:
#     swellData = []
#     windWaveData = []
#     formatted = None

# # Get latest data from NDBC using requests library
# def getLatestDataFromRequests():
#     url = 'https://www.ndbc.noaa.gov/data/latest_obs/46267.txt'
#     r = requests.get(url)
#     data = r.text
#     return data

# def populateBuoy():
#     data = getLatestDataFromRequests()
#     Buoy.formatted = data.replace('°', ' deg')
#     array = Buoy.formatted.split('\n')

#     for i in range(13, 16):
#         subArray = array[i].split(' ')
#         Buoy.swellData.append(subArray)

#     for i in range(16, 19):
#         subArray = array[i].split(' ')
#         Buoy.windWaveData.append(subArray)

# def checkSwell():
#     populateBuoy()
#     if float(Buoy.swellData[0][1]) > 0.5:
#         send("SURF ALERT\n" + Buoy.formatted)
#         print("Surf alert sent")

# checkSwell()

def alert():
    url = 'https://api.weather.gov/alerts'
    data = fetch_data(url)
    for alert in data['features']:
        # send(alert['properties']['headline'] + '\n' + alert['properties']['description'])
        print(data)

active = True

# Schedule the checkSwell function to run every 30 minutes
if active:
    # checkSwell
    schedule.every(30).minutes.do(alert)
    # schedule.every(30).minutes.do(checkSwell)

while True:
    schedule.run_pending()
    time.sleep(1)
