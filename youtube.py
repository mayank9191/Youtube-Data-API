from googleapiclient.discovery import build

API_KEY = "AIzaSyC8PxyjD2D5_ZiuMgAEJ8-wgFoOzDDZmbw"

youtube = build(
    'youtube',
    'v3',
    developerKey=API_KEY
)

# Make request to Youtube API

request = youtube.channels().list(
    part='statistics',
    forUsername=''
)

# Get a response from API

response = request.execute()

print(response)
