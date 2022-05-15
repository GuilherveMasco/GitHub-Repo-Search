import requests
import json
import sys


url = "https://api.github.com/search/repositories?q=topic:" + sys.argv[1]

headers = {
    'User': '###USERNAME###',
    'Authorization': '###TOKEN###'
}

response = requests.request("GET", url, headers=headers)


response_json = response.json()
print(response_json)

response_string = json.dumps(response_json)

with open('output.json', 'w') as outfile:
    outfile.write(response_string)