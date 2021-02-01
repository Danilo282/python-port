import requests
import OAuth1

url = "https://oet84792.live.dynatrace.com/api/config/v1/dashboards"
auth = OAuth1('7WavX8YTQlSSz7eTsWIfY')

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, auth=auth, headers=headers, data=payload)

print(response.text.encode('utf8'))
