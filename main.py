import argparse

import requests
import configparser
from pet import Pet
from utils import Util

config = configparser.ConfigParser()
config.read('data.properties')

url = "{url}?status={status_value}".format(url=config.get("data", "endpoint"),
                                           status_value=config.get("data", "status"))

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--name", help="your name")

args = argParser.parse_args()

print("args.name=%s" % args.name)


def print_pets_data(response):
    pets_data = []
    for x in response.json():
        try:
            a = Pet(x["id"], x["name"])
            pets_data.append(a)
        except:
            a = Pet(x["id"], None)
            pets_data.append(a)
            print("Name key is not defined for pet id = {id}".format(id=x["id"]))

    for p in pets_data:
        print(str(p))

    return pets_data


data = print_pets_data(response)

util = Util(data)

print(util.count_pets_names())

