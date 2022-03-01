
#! /usr/bin/env python3

import os
import requests
import json

headers = {
    'Content-type':'application/json',
    'Accept':'application/json'
}

desc_path = "./supplier-data/descriptions/"
for file in os.listdir(desc_path):
  print(file)
  list = ["name","weight","description"]
  dict ={}
  i = 0
  with open(desc_path+file, "r") as f:
    for line in f:
      if i == 1:
        line = int(line.replace("lbs",""))
      dict[list[i]] = line
      i += 1
      if i == len(list):
        break
    dict["image_name"] = file.replace(".txt",".jpeg")
    print("{}".format(json.dumps(dict)))
    response = requests.post("http://34.135.174.183/fruits/", data = json.dumps(dict), headers = headers)
    if not response.ok :
      raise Exception("Post Failed with status code {}".format(response.status_code))

