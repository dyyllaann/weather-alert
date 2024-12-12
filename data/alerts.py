import requests
import json
from pprint import pprint
from datetime import datetime, timezone

url = "https://api.weather.gov/alerts"

# def fetch_weather_alerts(url):
#     try:
#         # Make the GET request
#         response = requests.get(url)
        
#         # Check if the request was successful
#         response.raise_for_status()  # Raises an HTTPError for bad responses
        
#         # Parse JSON response
#         data = response.json()
        
#         return data
    
#     except requests.exceptions.HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Handle HTTP errors
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Handle other exceptions

def check_date(given_date):
    # Parse the string into a datetime object
    date_obj = datetime.fromisoformat(given_date)

    # Get the current date in the same timezone as the parsed date
    today_date = datetime.now(date_obj.tzinfo).date()

    # Compare the date parts
    is_today = date_obj.date() == today_date

    return is_today

def fetch_weather_alerts(zone):
    
    params = {
        "zone": zone
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        alerts = response.json().get("features", [])
        if alerts:
            for alert in alerts:
                date_str = alert["properties"]["effective"]

                if alert["properties"]["messageType"] == "Alert" and check_date(date_str):
                    print(alert["properties"]["messageType"] + ' for ' + alert["properties"]["areaDesc"])
                    print(alert["properties"]["headline"])
        else:
            print("No alerts at this time.")
    else:
        print("Error fetching data:", response.status_code)

# Fetch alerts for specific Washington zones
data = fetch_weather_alerts(zone="WAZ516,WAZ517,WAZ510")
