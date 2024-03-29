import datetime
import os

import cairosvg
import requests

from project_config.config import RAPID_API_KEY, RAPID_API_URL
from utils.coinranking_api.path_n_clean import path_to_temp
from database.coins_name_db import select_data

from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen


def coin_info(
    add_url: str = "coin",
    coin_name: str = "eth",
    referenceCurrencyUuid: str = "yhjMzLPhuIDl",
    timePeriod: str = "5y",
) -> tuple[dict, str]:
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

    api_uuid = select_data(coin_name=coin_name.lower().replace(" ", ""))
    url = RAPID_API_URL + add_url + "/" + api_uuid

    querystring = {
        "referenceCurrencyUuid": referenceCurrencyUuid,
        "timePeriod": timePeriod,
    }

    headers = {"X-RapidAPI-Key": RAPID_API_KEY}

    response = requests.get(url, headers=headers, params=querystring)
    return response.json(), timePeriod


def symbol_picture(url: str) -> str:
    """
    Convert a ".SVG" image to a ".PNG" image

    :param url: url to image
    :return: path to converted image
    """
    folder = path_to_temp()
    if ".svg" in url.split("/")[-1]:
        req = requests.get(url)
        with open(folder + url.split("/")[-1], "wb") as image:
            image.write(req.content)
        svg_image_name = url.split("/")[-1].split(".")[0]
        cairosvg.svg2png(
            url=folder + svg_image_name + ".svg",
            write_to=folder + svg_image_name + ".png",
        )
        path = folder + svg_image_name + ".png"
        os.remove(folder + svg_image_name + ".svg")
    else:
        image = Image.open(urlopen(url))
        image.save(folder + url.split("/")[-1])
        path = folder + url.split("/")[-1]
    image = Image.open(path)
    image = image.resize((60, 60))
    image.save(path)
    return path


def put_image_in_image(path_img1: str, path_img2: str) -> None:
    """
    Paste a coin label to a plot image

    :param path_img1: plot (main) image
    :param path_img2: coin label image
    :return: None
    """
    img1 = Image.open(path_img1)
    img2 = Image.open(path_img2)
    img1.paste(img2, (3, 3))
    img1.save(path_img1)


def create_graph(info: [dict, str]) -> str:
    """
    Create cost plot for a coin

    :param info: coin info and time period
    :return: path to plot
    """
    folder = path_to_temp()
    data = info[0]
    y_coord = []
    for elem in data["data"]["coin"]["sparkline"]:
        try:
            y_coord_cur = float(elem)
            y_coord.append(y_coord_cur)
        except TypeError:
            y_coord_cur = 0
            y_coord.append(y_coord_cur)
    x_coord = [elem for elem in range(len(data["data"]["coin"]["sparkline"]))]

    fig, ax = plt.subplots()
    symbol_url = data["data"]["coin"]["iconUrl"]
    image = symbol_picture(url=symbol_url)
    ax.plot(
        x_coord,
        y_coord,
        color="black",
        ls="--",
        linewidth=3,
        marker="o",
        markersize=4,
        markerfacecolor="red",
    )
    plt.title(f"{data['data']['coin']['name']} ({data['data']['coin']['symbol']})")
    plt.xlabel(f"Time period, {info[1]}")
    plt.ylabel("Coast, $")
    plt.minorticks_on()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    path = folder + str(datetime.datetime.now()) + "_" + "graph.png"
    plt.savefig(path)
    put_image_in_image(path_img1=path, path_img2=image)
    os.remove(image)
    return path


def coin_info_output(
    coin_name: str = "eth", time_period: str = "5y"
) -> tuple[str, str]:
    """
    Output info about user's response coin

    :param coin_name: name of a coin
    :param time_period: time period in API format (exm., 5y)
    :return: description and path to photo
    """
    try:
        data = coin_info(coin_name=coin_name, timePeriod=time_period)
        picture = create_graph(info=data)
        text = (
            f"💰price: {round(float(data[0]['data']['coin']['price']), 4)}\n"
            f"🔺🔻change, %: {data[0]['data']['coin']['change']}\n"
            f"🔗price to BTC: {round(float(data[0]['data']['coin']['btcPrice']), 4)}\n"
            f"🌎website: {data[0]['data']['coin']['websiteUrl']}"
        )

        return text, picture
    except TypeError:
        img = Image.new(mode="RGB", size=(300, 300), color="#FFEFD5")
        draw_img = ImageDraw.Draw(im=img)
        fnt = ImageFont.truetype("FreeMono.ttf", 40)
        draw_img.text(xy=(90, 120), text="ERROR", font=fnt, fill="#8B0000")

        path = f"{path_to_temp()}{datetime.datetime.now()}_history.png"
        img.save(path)
        return (
            f"This token doesn't exist, please check it\n"
            f"Maybe command \\start will resolve this"
        ), path


if __name__ == "__main__":
    print(coin_info_output())
