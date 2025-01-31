import requests

API_KEY = "AIzaSyC8PxyjD2D5_ZiuMgAEJ8-wgFoOzDDZmbw"


query = "carryminati"
URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={
    query}&type=video&key={API_KEY}"

response = requests.get(url=URL)


response.raise_for_status()

print(response.text)
