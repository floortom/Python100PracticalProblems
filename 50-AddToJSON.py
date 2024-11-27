import json
import pprint

with open("company.json", "r+") as file:
    workers = json.loads(file.read())
    workers["employees"].append({"firstName": "Albert",
                                 "lastName":  "Bert"})
    file.seek(0)
    json.dump(workers, file, indent=4, sort_keys=True)
    file.close()
