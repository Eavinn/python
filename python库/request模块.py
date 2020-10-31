import requests
import json

session = requests.session()
post_url = "http://127.0.0.1:5000"
data = {"aa": "meng"}

r = session.post(url=post_url, data=data)
print(r.text)
