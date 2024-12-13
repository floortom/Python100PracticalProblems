import requests
import urllib3
urllib3.disable_warnings()
r = requests.get("https://pythonhow.com/media/data/universe.txt", verify=False)
print(r.text)
