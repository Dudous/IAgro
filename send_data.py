import json
import random
import requests

back_url = 'back_do_fer'

with open('./data.json', 'r') as file:
    data = json.load(file)

    for coord in data.keys():
        data[coord] = 1 if random.random() < 0.4 else 0

with open('./data.json', 'w') as file:
    file.write(json.dumps(data))


res = requests.post(back_url,
    data=data
)

print(res.json())