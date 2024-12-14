from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import schedule
import requests
from notifier import send
from data.alerts import fetch_weather_alerts

# Check for weather alerts. If an alert is active, send an alert
def alert():
    send(fetch_weather_alerts(zone="WAZ516,WAZ517,WAZ510"))

active = True

# Schedule the alert function to run every hour
if active:
    alert()
    schedule.every().hour.do(alert)

while True:
    schedule.run_pending()
    time.sleep(1)
