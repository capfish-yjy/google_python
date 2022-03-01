
#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
image_path = "./supplier-data/images/"
for file in os.listdir(image_path):
  if file.endswith(".jpeg"):
    print(file)
    with open(image_path+file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
