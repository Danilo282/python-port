import requests

url = "http://34.121.238.96:4440/api/21/job/c8cc9270-a333-4a9b-9957-82f6527678e5/run"

payload = {}
headers = {
  'Accept': 'application/json',
  'X-Rundeck-Auth-Token': 'VXK4mL96Vo3kEDhH2fZrNTUDoFif4CUo',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))