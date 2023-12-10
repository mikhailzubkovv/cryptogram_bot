import datetime

from sqlalchemy import Column, Integer, String
from PIL import Image, ImageDraw

from database.connect_to_db import connect_db, Base
from utils.coinranking_api.path_n_clean import path_to_temp


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


def select_data(user_name: int) -> list | str:
    """
    Select all user's history from DB by user_id

    :param user_name: user_id in telegram
    :return: ???????????????????????????? TODO
    """
    session = connect_db()
    try:
        history = session.query(UserHistory).filter(UserHistory.user_name == user_name).all()
        text = [('user_name', 'module', 'coin_name', 'time_period', 'amount_output', 'update_date')]

        for pos, hist_elem in enumerate(history):
            if pos in (elem for elem in range(len(history) - 10, len(history) + 1)):
                text.append((hist_elem.user_name, hist_elem.module, hist_elem.coin_name, hist_elem.time_period,
                             hist_elem.amount_output, hist_elem.update_date))
        return text
    except AttributeError:
        return "Sorry, You don't have a saved history yet"


def print_pretty_table(data: list, cell_sep=' | ', header_separator=True) -> str:
    """
    Function to create a readable output format for DB content

    :param data: info from DB with headers
    :param cell_sep: separator for data
    :param header_separator: separator for header
    :return: text to output
    """
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)
    text = ''
    for pos, row in enumerate(range(rows)):
        if pos == 1 and header_separator:
            text += separator
            text += '\n'

        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)

        text += cell_sep.join(result)
        text += '\n'

    return text


def text_to_picture(text: str) -> None:
    img = Image.new(mode='RGB', size=(800, 800), color='#83A2FF')
    draw_img = ImageDraw.Draw(im=img)
    draw_img.text(
        xy=(0, 0),
        text=text,
        fill='#1C0606'
    )
    img.show()


if __name__ == '__main__':
    info = select_data(user_name=958241070)
    output = print_pretty_table(data=info, header_separator=True)
    print(output)
    text_to_picture(text=output)
