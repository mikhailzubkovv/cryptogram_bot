from sqlalchemy import Column, Integer, String

from database.connect_to_db import connect_db, Base


class UserHistory(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'user_history'

    id_position = Column(Integer, primary_key=True)
    user_name = Column(Integer)
    module = Column(String(250))
    coin_name = Column(String(250))
    time_period = Column(String(250))
    amount_output = Column(String(250))
    update_date = Column(String(250))

    def __init__(self, user_name, module, coin_name, time_period, amount_output, update_date) -> None:
        self.user_name = user_name
        self.module = module
        self.coin_name = coin_name
        self.time_period = time_period
        self.amount_output = amount_output
        self.update_date = update_date


def add_to_db(
        user_name: int,
        module: str,
        coin_name: str,
        time_period: str,
        amount_output: str,
        update_date: str
) -> None:
    """
    Upload info to DB.
    """
    session = connect_db()
    history = UserHistory(
        user_name=user_name,
        module=module,
        coin_name=coin_name,
        time_period=time_period,
        amount_output=amount_output,
        update_date=update_date)
    session.add(history)
    session.commit()


def select_data(user_name: int) -> str | None:
    session = connect_db()
    try:
        history = session.query(UserHistory).filter(UserHistory.user_name == user_name).all()

        text = ''
        for pos, hist_elem in enumerate(history):
            if pos in (elem for elem in range(len(history) - 10, len(history) + 1)):
                text += (f'| {hist_elem.user_name} | {hist_elem.module} | {hist_elem.coin_name} |'
                         f' {hist_elem.time_period} | {hist_elem.amount_output} | {hist_elem.update_date} |\n')
        return text
    except AttributeError:
        return "Sorry, You don't have saved history yet"


if __name__ == '__main__':
    print(select_data(user_name=958241070))
