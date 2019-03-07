import requests
r = requests.get('https://kufar.by')
assert r.status_code == 200, "error"
r1 = requests.get('https://vk.com')
assert r.status_code == 200, "ERROR"
r2 = requests.get('https://onliner.by')
if(r.status_code == 200):
	print("nice")