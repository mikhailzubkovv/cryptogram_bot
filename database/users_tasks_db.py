from sqlalchemy import Column, Integer, String

from database.connect_to_db import connect_db, Base


class UsersTask(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'users_tasks'

    id_position = Column(Integer, primary_key=True)
    user_name = Column(Integer)
    coin_name = Column(String(250))
    time_period = Column(String(250))
    repeat_time = Column(String(250))

    def __init__(self, user_name, coin_name, time_period, repeat_time) -> None:
        self.user_name = user_name
        self.coin_name = coin_name
        self.time_period = time_period
        self.repeat_time = repeat_time


def add_to_db(
        user_name: int,
        coin_name: str,
        time_period: str,
        repeat_time: str
) -> None:
    """
    Upload dict to DB.
    """
    session = connect_db()
    task = UsersTask(user_name=user_name, coin_name=coin_name, time_period=time_period, repeat_time=repeat_time)
    session.add(task)
    session.commit()


def drop_from_db(id_position: int, user_name: int) -> None:
    """
    Delete task's record from DB

    :param id_position: position of tasks - id_key in PSQL
    :param user_name: user_name - username in TG system to forbid delete others records
    :return: None
    """
    session = connect_db()
    try:
        task = session.query(UsersTask).get(id_position)
        if task.user_name == user_name:
            session.delete(task)
    except Exception:
        pass
    session.commit()


def select_data(user_name: int) -> dict:
    """
    Select all tasks for user from DB

    :param user_name: username in TG system
    :return: dictionary with user's tasks
    """
    session = connect_db()
    users_tasks = {}
    try:
        tasks = session.query(UsersTask).filter(UsersTask.user_name == user_name).all()
        for task in tasks:
            users_tasks[task.id_position] = {
                'coin_name': task.coin_name,
                'time_period': task.time_period,
                'repeat_time': task.repeat_time
            }

        return users_tasks
    except AttributeError:
        pass


if __name__ == '__main__':
    select_data(user_name=958241070)
