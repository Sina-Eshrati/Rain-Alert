import requests
from twilio.rest import Client

parameters = {
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "lat": 41.693630,
    "lon": 44.801620,
    "exclude": "current,minutely,daily"
}

account_sid = "AC6d066e58affc4e3fc06332a66c630e25"
auth_token = "d3934e03fbef686a19dc3250980e5618"

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data["hourly"][:12]
will_rain = False

for each_hour in weather_data:
    if each_hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+15628421413',
        to='+995593601624'
    )
    print(message.status)