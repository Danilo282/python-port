import requests
import requests_debugger

requests_debugger.set(output_format=requests_debugger.CURL, max_depth=0)

url = 'https://seusaas.live.dynatrace.com/api/v1/problem/status'

r = requests.get(url,
                 headers={'Authorization':
                          'Api-Token '})

r.json()
