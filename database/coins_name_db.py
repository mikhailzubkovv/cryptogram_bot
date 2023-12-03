import time

from sqlalchemy import Column, Integer, String

from database.connect_to_db import connect_db, Base


class CoinsNames(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'coins_names'

    id_position = Column(Integer, primary_key=True)
    name = Column(String(250))
    api_uuid = Column(String(250))

    def __init__(self, name, api_uuid) -> None:
        self.name = name
        self.api_uuid = api_uuid


def add_to_db(name: str, api_uuid: str) -> None:
    """
    Upload dict to DB.
    """
    session = connect_db()
    coin_name = CoinsNames(name=name, api_uuid=api_uuid)
    session.add(coin_name)
    session.commit()


def select_data(coin_name: str) -> str:
    session = connect_db()
    coin = session.query(CoinsNames).filter(CoinsNames.name == coin_name).first()
    return coin.api_uuid


if __name__ == '__main__':
    pass
