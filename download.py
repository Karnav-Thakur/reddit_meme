import requests
import os
import aiohttp
import asyncio
session = aiohttp.ClientSession()

def url_refresh(url):
    return url

async def main():
    list_dir = os.listdir('./meme')
    len_list_dir = len(list_dir)
    for i in range(len_list_dir,2*len_list_dir):
        url = url_refresh('https://www.reddit.com/r/memes/random/.json')
        r = await session.get(url)
        josn = await r.json(content_type=None)
        if r.status == 200:
            print(i)
            link = josn[0]['data']['children'][0]['data']['preview']['images'][0]['source']['url']
            with open(f'./meme/meme{i}.jpg' , 'wb') as f:
                try:
                    link = link.split('//')[1]
                    link = link.replace("amp;", "")
                    im = requests.get(f"http://{link}")
                except IndexError:
                    continue
                im_content = im.content
                f.write(im_content)
        else:
            continue
            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())