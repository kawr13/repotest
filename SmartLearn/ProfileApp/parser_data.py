import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote
from icecream import ic

URL = 'https://www.youtube.com/results?search_query='


async def get_html(url):
    headers = {
        'Accept-Encoding': 'utf-8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    # url = quote(url, safe=':/?=&')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.read()
                return html


async def get_content(html):
    dicting = {}
    soup = bs(html, 'lxml')

    ic(soup['watchEndpointSupportedOnesieConfig']['html5PlaybackOnesieConfig']['commonConfig']['url'])

async def serialize(data):
    pass


async def main(url):
    data_url = await get_html(url)
    urls = await get_content(data_url)


def pars_start():
    request = 'python уроки'
    new_request = request.replace(' ', '+')
    url = URL + new_request
    data = asyncio.run(main(url))


if __name__ == '__main__':
    pars_start()