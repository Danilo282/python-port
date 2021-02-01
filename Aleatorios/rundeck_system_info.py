import requests

url = "http://34.121.238.96:4440/api/21/system/info"

payload = {}
files = {}
headers = {
  'Accept': 'application/json',
  'X-Rundeck-Auth-Token': 'VXK4mL96Vo3kEDhH2fZrNTUDoFif4CUo'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))