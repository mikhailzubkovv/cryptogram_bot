from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from database.config_db import username_db, password_db, host_db, port_db, db_name

Base = declarative_base()


def connect_db():
    engine = create_engine(f'postgresql+psycopg://{username_db}:{password_db}@{host_db}:{port_db}/{db_name}')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return Session()


if __name__ == '__main__':
    connect_db()

