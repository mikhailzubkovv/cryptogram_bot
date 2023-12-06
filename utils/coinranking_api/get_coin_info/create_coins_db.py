from utils.coinranking_api.coins_list import get_all_coins
from database.coins_name_db import add_to_db


def create_coins_db() -> None:
    data = get_all_coins(timePeriod='5y', limit='5000')

    for values in data['data']['coins']:
        add_to_db(
            name=values['symbol'].lower().replace(' ', ''),
            api_uuid=values['uuid']
        )

        add_to_db(
            name=values['name'].lower().replace(' ', ''),
            api_uuid=values['uuid']
        )


if __name__ == '__main__':
    create_coins_db()
