import requests
from datetime import datetime
# Response codes simplified
# 1XX - Hold on
# 2XX - Here you go
# 3XX - Go Away
# 4XX - You screwed up
# 5XX - I screwed up (some server issue)

# Simple example of API without parameters
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]


print(f"{latitude} {longitude} ")

# Example with parameters
parameters = {
    "lat": "-29.6604",
    "lng": "-51.0562",
    "formatted": "0",
    "tzid": "America/Sao_Paulo"
}
response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(f"{sunrise} {sunset}")


time_now = datetime.now()
print(time_now.hour)

