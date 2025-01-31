import requests
import ffmpeg
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Referer": "https://javct.net/",  # Replace with the actual referring site
    "Accept": "*/*",
    "Connection": "keep-alive"
}


for i in range(1, 736):
    url = f'''https://5r9v2dkjs3dcq.milocdn.com/hls2/01/03733/hxize6pxav1i_,l,n,h,.urlset/seg-{
        i}-f2-v1-a1.ts?t=AqJENSlmeU5tNtcLLVNT9Y4T1dsbgwpamcEmB7x-DCs&s=1738270524&e=129600&f=18667023&srv=oEnCfSroTWl07&i=0.4&sp=500&p1=oEnCfSroTWl07&p2=oEnCfSroTWl07&asn=24560'''
    response = requests.get(url, stream=True)

    with open(f"downloads/segment_{i}.mp4", "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)


video_files = []
for i in range(1, 736):
    video_files.append(f"downloads/segment_{i}.mp4")


with open("file_list.txt", "w") as f:
    for file in video_files:
        f.write(f"file '{file}'\n")

# Merge MP4 files without re-encoding
output_file = "merged.mp4"
ffmpeg.input("file_list.txt", format="concat",
             safe=0).output(output_file, c="copy").run()

print(f"Merged video saved as {output_file}")
