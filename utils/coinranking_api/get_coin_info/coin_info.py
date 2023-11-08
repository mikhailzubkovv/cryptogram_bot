import json
import os
import cairosvg
import requests

from utils.coinranking_api.config import RAPID_API_KEY, RAPID_API_URL
from utils.coinranking_api.get_coin_info.create_coins_db import create_coins_db
from matplotlib import pyplot as plt
from PIL import Image
from urllib.request import urlopen


def coin_info(
        add_url: str = 'coin',
        coin_name: str = 'btc',
        referenceCurrencyUuid: str = 'yhjMzLPhuIDl',
        timePeriod: str = '5y'
) -> dict:
    """
    Get a coin info from Coinranking.com API.

    :param coin_name: coin name for building API access
    :param add_url: additional text to url
    :param referenceCurrencyUuid: UUID of reference currency, in which all the prices are calculated.
    This includes the price, the change and the sparkline. Defaults to US Dollar
    :param timePeriod: By setting the timePeriod the change percentage and sparkline in the response will be
    calculated accordingly
        Default value: 24h
        Allowed values:
        1h 3h 12h 24h 7d 30d 3m 1y 3y 5y

    :return: full response content from Coinranking.com for a coin
    """

    create_coins_db()
    with open('coins_name_db.json', 'r') as file:
        data = json.load(file)
    url = RAPID_API_URL + add_url + '/' + data[coin_name.lower()]

    querystring = {
        "referenceCurrencyUuid": referenceCurrencyUuid,
        "timePeriod": timePeriod
    }

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY
    }

    response = requests.get(url, headers=headers, params=querystring)
    with open('coin_info.json', 'w') as file:
        json.dump(response.json(), file, indent=4)


def symbol_picture(url: str) -> str:
    if '.svg' in url.split('/')[-1]:
        req = requests.get(url)
        with open(url.split('/')[-1], 'wb') as image:
            image.write(req.content)
        svg_image_name = url.split('/')[-1].split('.')[0]
        cairosvg.svg2png(url=svg_image_name + '.svg', write_to=svg_image_name + '.png')
        path = svg_image_name + '.png'
        os.remove(svg_image_name + '.svg')
    else:
        image = Image.open(urlopen(url))
        image.save(url.split('/')[-1])
        path = url.split('/')[-1]
    return path


def create_graph() -> None:
    with open('coin_info.json', 'r') as file:
        data = json.load(file)

    y_coord = []
    for elem in data['data']['coin']['sparkline']:
        try:
            y_coord_cur = float(elem)
            y_coord.append(y_coord_cur)
        except TypeError:
            y_coord_cur = 0
            y_coord.append(y_coord_cur)
    x_coord = [elem for elem in range(len(data['data']['coin']['sparkline']))]

    fig, ax = plt.subplots()
    symbol_url = data['data']['coin']['iconUrl']
    image = symbol_picture(url=symbol_url)
    img = plt.imread(image)
    ax.imshow(img, extent=[min(x_coord), max(x_coord) + 1, min(y_coord), max(y_coord)], aspect='auto')
    fig.patch.set_facecolor(data['data']['coin']['color'])
    ax.plot(x_coord, y_coord, '--p', linewidth=4)
    plt.title(f"{data['data']['coin']['name']} ({data['data']['coin']['symbol']})")
    plt.xlabel('Time period (hours/months)')
    plt.ylabel('Coast, $')
    plt.savefig('graph.png')
    os.remove(image)


if __name__ == '__main__':
    # coin_info()
    create_graph()
    # img = symbol_picture(url='https://cdn.coinranking.com/xcZdYtX6E/okx.png')
    # img.show()
