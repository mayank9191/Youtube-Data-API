import requests
# Script to download song in stream format

url = "https://aac.saavncdn.com/815/483a6e118e8108cbb3e5cd8701674f32_160.mp4"

# https://aac.saavncdn.com/815/483a6e118e8108cbb3e5cd8701674f32_160.mp4

response = requests.get(url=url, stream=True)


with open("sound1.mp4", "wb") as f:
    for chunk in response.iter_content(chunk_size=256):
        f.write(chunk)


# print(response.text)


# This is helpful code to get streams
