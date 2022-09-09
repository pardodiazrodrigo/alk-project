import pandas
import psycopg2
import sqlalchemy.engine
from sqlalchemy import create_engine, exc
from settings import DB_INFO
from datetime import date
from sqlalchemy_utils import database_exists, create_database


def create_db(db_location: str) -> None:

    try:
        if not database_exists(db_location):
            create_database(db_location)
    except Exception as e:
        print(e)


def create_tables(path_sql: str) -> None:

    try:
        with psycopg2.connect(host=DB_INFO['host'],
                              user=DB_INFO['user'],
                              password=DB_INFO['password'],
                              database=DB_INFO['dbname']) as conn:

            conn.autocommit = True

            with conn.cursor() as cursor:
                with open(path_sql, 'r') as f:
                    data = f.read()
                    cursor.execute(data)
    except Exception as e:
        print(e)


def get_engine(db_info) -> sqlalchemy.engine.Engine:
    engine = create_engine(db_info)
    return engine


def update_database(db_location: str, df: pandas.DataFrame, table_name: str) -> None:
    df['fecha_de_carga'] = date.today().strftime("%d-%m-%Y")

    try:
        df.to_sql(table_name, get_engine(db_location), if_exists='replace', index=False)
    except exc.SQLAlchemyError as e:
        print(e)
