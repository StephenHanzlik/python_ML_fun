import requests
import os

dataset_id = 'ds_bzrxwxbgp6100ehas4eg'
api_key = os.environ.get('SCALE_API_KEY')

response = requests.get(
    f"https://api.scale.com/v1/nucleus/dataset/{dataset_id}/info",
    json={},
    headers={"Content-Type": "application/json"},
    auth=(api_key, ""),
)

print(response.json())