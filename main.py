import requests as req
from bs4 import BeautifulSoup
import asyncio
import time

async def download_image(image_url, name):
    img = req.get(image_url).content
    with open(f'image/image_{name}.jpg', "wb+") as f:
        f.write(img)


async def find_image_urls(soup: BeautifulSoup, download: bool, class_value: str):
    counter = 0
    image_results = soup.find_all("a", class_value)

    for image_result in image_results:
        if download:
            asyncio.create_task(
                download_image(image_result['href'], counter))
        else:
            print(image_result['href'])
        counter += 1

async def main():
    url = input("Enter url to download images from: ")
    class_value = input("Enter class value of <a> tag: ")
    download = input("Should download? (True/False): ")
    page = req.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    task = asyncio.create_task(find_image_urls(soup, download, class_value))
    print(f"Started at {time.strftime('%X')}")

    await task

    print(f"Finished at {time.strftime('%X')}")

if __name__ == '__main__': 
    asyncio.run(main())