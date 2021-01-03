import requests
import os

api_key = os.environ.get('SCALE_API_KEY')

payload = {
  "name": "North West Spring 2019 Dataset"
}

response = requests.post(
    "https://api.scale.com/v1/nucleus/dataset/create",
    json=payload,
    headers={"Content-Type": "application/json"},
    auth=(api_key, ""),
)
print(response.json())
#'dataset_id': 'ds_bzrxwxbgp6100ehas4eg'