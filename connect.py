import os
import requests
import time
from generate_code import generateCode

check_existence_path = f'http://localhost:5215/api/devices/{generateCode()}'

while requests.get(check_existence_path).status_code == 204:
    print(204)
    time.sleep(1)

print('vai tomando')