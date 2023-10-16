import requests
import json

from utils.coinranking_api.config import RAPID_API_KEY, RAPID_API_URL


def get_all_coins(
        add_url: str = 'coins',
        referenceCurrencyUuid: str = 'yhjMzLPhuIDl',
        timePeriod: str = '24h',
        tiers: str = '1',
        orderBy: str = 'price',
        orderDirection: str = 'desc',
        limit: str = '5',
        offset: str = '0'

) -> None:
    """

    :param add_url:
    :param referenceCurrencyUuid:
    :param timePeriod:
    :param tiers:
    :param orderBy:
    :param orderDirection:
    :param limit:
    :param offset:
    :return:
    """

    url = RAPID_API_URL + add_url

    querystring = {
        "referenceCurrencyUuid": referenceCurrencyUuid,
        "timePeriod": timePeriod,
        "tiers[0]": tiers,
        "orderBy": orderBy,
        "orderDirection": orderDirection,
        "limit": limit,
        "offset": offset
    }

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY
    }

    response = requests.get(url, headers=headers, params=querystring)
    # print(response.json())

    data = json.loads(response.text)
    with open('all_coins.json', 'w') as file:
        json.dump(data, file, indent=4)


def write_to_db():
    ...


def print_to_user_top(user_top: int) -> str:
    with open('utils/coinranking_api/get_all_coins/all_coins.json', 'r') as file:
        data: dict = json.load(file)

    if len(data['data']['coins']) <= user_top:
        user_top = len(data['data']['coins'])

    message_text = ''

    for position, value in enumerate(data['data']['coins']):
        # print(f'pos{position}, val {value}')

        text = (f"🔘{value['name']}\n"
                f"  CALCULATE PERIOD {'TO DO'}\n"
                f"  💰avg price, USD: {round(float(value['price']), 2)}\n"
                f"  🔄change price, %: {round(float(value['change']), 2)}\n"
                f"  💱price to BTC: {round(float(value['btcPrice']), 4)}\n"
                f"\n")
        message_text += text
        # print(text)
        if position + 1 >= user_top:
            break
    return message_text


if __name__ == '__main__':
    # get_all_coins()
    print_to_user_top(user_top=4)
