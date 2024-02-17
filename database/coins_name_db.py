from sqlalchemy import Column, Integer, String

from database.connect_to_db import connect_db, Base


class CoinsNames(Base):
    """
    Create table in DB with Column below.
    """

    __tablename__ = "coins_names"

    id_position = Column(Integer, primary_key=True)
    name = Column(String(250))
    api_uuid = Column(String(250))
    update_date = Column(String(250))

    def __init__(self, name, api_uuid, update_date) -> None:
        self.name = name
        self.api_uuid = api_uuid
        self.update_date = update_date


def add_to_db(name: str, api_uuid: str, update_date: str) -> None:
    """
    Upload dict to DB.
    """
    session = connect_db()
    coin_name = CoinsNames(name=name, api_uuid=api_uuid, update_date=update_date)
    session.add(coin_name)
    session.commit()


def select_data(coin_name: str) -> str:
    """
    Select coin's UUID key from DB by coin's name

    :param coin_name: coin's name from user's input
    :return: UUID key for Coinranking API
    """
    session = connect_db()
    try:
        coin = session.query(CoinsNames).filter(CoinsNames.name == coin_name).first()
        return coin.api_uuid
    except AttributeError:
        pass


def checkout_db() -> str:
    """
    Checkout existing DB with coin's names

    :return: last update date or State 1 (DB is not exist)
    """
    session = connect_db()
    try:
        coin = session.query(CoinsNames).filter(CoinsNames.id_position == 1).first()
        return coin.update_date
    except AttributeError:
        return "1"


if __name__ == "__main__":
    pass
