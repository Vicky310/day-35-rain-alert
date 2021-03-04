import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR OWM API KEY"
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"
LAT = 52.939915
LONG = -73.549133

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! Remember to bring an Umberlla!",
        from_='+14844696948',
        to='+15199928272'
    )
    print(message.status)