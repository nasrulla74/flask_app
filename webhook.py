import requests
import json

webhook_url = "https://flask-app-lveg.onrender.com/webhook"

data = { 'name': 'Nasrulla',
         'chanel_url': 'test url'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

