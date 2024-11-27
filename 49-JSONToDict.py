import json
import pprint

with open("company.json", "r") as file:
    workers = json.loads(file.read())
    pprint.pprint(workers)
