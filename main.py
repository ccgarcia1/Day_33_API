import requests
# Response codes simplified
# 1XX - Hold on
# 2XX - Here you go
# 3XX - Go Away
# 4XX - You screwed up
# 5XX - I screwed up (some server issue)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]


print(f"{latitude} {longitude} ")

