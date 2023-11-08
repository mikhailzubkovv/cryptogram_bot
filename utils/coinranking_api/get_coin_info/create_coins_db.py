import json

from utils.coinranking_api.coins_list import get_all_coins


def create_coins_db() -> None:
    data = get_all_coins(timePeriod='5y', limit='5000')

    coins_names = {}
    for values in data['data']['coins']:
        coins_names[values['symbol'].lower().replace(' ', '')] = values['uuid']
        coins_names[values['name'].lower().replace(' ', '')] = values['uuid']

    with open('coins_name_db.json', 'w') as file:
        json.dump(coins_names, file, indent=4)


if __name__ == '__main__':
    create_coins_db()
