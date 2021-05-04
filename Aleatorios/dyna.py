import requests
import requests_debugger

requests_debugger.set(output_format=requests_debugger.CURL, max_depth=0)

url = 'https://zxu81723.live.dynatrace.com/api/v1/problem/status'

r = requests.get(url,
                 headers={'Authorization':
                          'Api-Token dt0c01.JK2EK54TFCXRHHULFJCAIVUB.H6C3KKNX47FOWUKKOK6COHQDVFLQODO7LIGKZQBTMYRWJTO6XUQSPFIVU5M56MY4'})

r.json()
