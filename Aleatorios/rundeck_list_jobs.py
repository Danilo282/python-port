import requests

url = "http://34.121.238.96:4440/api/21/project/scripts/jobs"

payload = {}
files = {}
headers = {
  'Accept': 'application/json',
  'X-Rundeck-Auth-Token': 'VXK4mL96Vo3kEDhH2fZrNTUDoFif4CUo',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text.encode('utf8'))
