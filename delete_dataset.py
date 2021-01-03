import requests
import os

api_key = os.environ.get('SCALE_API_KEY')

response = requests.delete(
    "https://api.scale.com/v1/nucleus/dataset/ds_bzr94286c8ng099j8nj0",
    json={},
    headers={"Content-Type": "application/json"},
    auth=(api_key, ""),
)

print(response.json())
