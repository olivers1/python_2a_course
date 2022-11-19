import json

with open("services.json", "r") as file:
    services = json.load(file)

for item in services["services"]:
    if item["id"] == "36":
        print(item["title"])