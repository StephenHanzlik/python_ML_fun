import requests
import os
import json

dataset_id = 'ds_bzr92pagp610060y41qg'
api_key = os.environ.get('SCALE_API_KEY')

images = ("https://drive.google.com/file/d/19OuWm9AIXYN2TdP3960yplg0mJCZF5_s", 
"https://drive.google.com/file/d/1fJHPMbPWoAe1M6xIpoW4OxAQTBp0yw8q",
"https://drive.google.com/file/d/1dPvs0BOYnYzspf5c20fZbnSagzAddMHh",
"https://drive.google.com/file/d/1SIEX3VUzW6NRPP-_QDiC2N4KDUavUqZq",
"https://drive.google.com/file/d/1a3kP7PbWvzrLag9wDJHFh4AV5vlniK-f",
"https://drive.google.com/file/d/1tWFfAlrDhbnHKbgXJ3_lD6kvWt8WUpCU"
)

items = []
image_ref_number = 0

for image_url in images:
  image_ref_number += 1
  item = {
    "image_url": image_url,
    "reference_id": f"image_reference{image_ref_number}",
    "metadata": {
    "state": "Washington",
      "year": 2019
    },
  }
  items.append(item)

payload = {}
payload["items"] = items

response = requests.post(
    f"https://api.scale.com/v1/nucleus/dataset/{dataset_id}/append",
    json=payload,
    headers={"Content-Type": "application/json"},
    auth=(api_key, ""),
)

print(response.json())