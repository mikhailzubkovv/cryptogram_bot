import psycopg
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, declarative_base

from project_config.config import username_db, password_db, db_name

Base = declarative_base()


def connect_db():
    """
    Create connect to DB PSQL
    :return: Session object
    """
    try:
        # connection for docker mode. psql_database - container name for PSQL from docker-compose.yml file
        engine = create_engine(f'postgresql+psycopg://{username_db}:{password_db}@psql_database/{db_name}')
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
    except Exception:
        # connection to local PSQL server by local host
        engine = create_engine(f'postgresql+psycopg://{username_db}:{password_db}@localhost/{db_name}')
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
    return Session()


if __name__ == '__main__':
    connect_db()

