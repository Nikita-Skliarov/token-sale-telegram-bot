# This file parses json and return it as array
import json
with open("include/prices.json", "r", encoding="utf-8") as json_data:
    coins_data = json.load(json_data)