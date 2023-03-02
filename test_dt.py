import datetime
import requests

response = requests.get('https://api.arcadakms.ru/getInlifeInfo')
data = response.json()

events = data.get('data').get('events')

for event in events:
    print(event.get('date_time'))

res = events
# print(res)