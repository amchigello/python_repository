import requests
url="https://api.covid19india.org/states_daily.json"
response = requests.get(url).json()
print(response)