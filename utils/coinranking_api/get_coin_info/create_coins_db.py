import datetime

from utils.coinranking_api.coins_list import get_all_coins
from database.coins_name_db import add_to_db, checkout_db


def create_coins_db() -> None:
    data = get_all_coins(timePeriod='5y', limit='5000')

    last_date = format_date(checkout_db())
    today = format_date(date=str(datetime.date.today()))
    for values in data['data']['coins']:
        if last_date is None or today - last_date >= 5:
            add_to_db(
                name=values['symbol'].lower().replace(' ', ''),
                api_uuid=values['uuid'],
                update_date=str(datetime.date.today())
            )

            add_to_db(
                name=values['name'].lower().replace(' ', ''),
                api_uuid=values['uuid'],
                update_date=str(datetime.date.today())
            )
        else:
            pass


def format_date(date: str) -> int:
    return sum(map(int, date.split('-')))


if __name__ == '__main__':
    create_coins_db()
