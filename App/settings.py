from pathlib import Path
from decouple import config

BASE_DIR = Path().resolve()

# - URLS

URL_MUSEOS = config('URL_MUSEOS')
URL_SALAS_DE_CINE = config('URL_SALAS_DE_CINE')
URL_BIBLIOTECAS_POPULARES = config('URL_BIBLIOTECAS_POPULARES')

URL_NAMES = {"bibliotecas": URL_BIBLIOTECAS_POPULARES,
             "cines": URL_SALAS_DE_CINE,
             "museos": URL_MUSEOS}

# - DATA STORAGE

PATH_DATA = f"{BASE_DIR}/Data"

# - SQL SCRIPTS

SQL_PATH = f"{BASE_DIR}/sql/create_tables.sql"

# - DDBB

DB_INFO = {"host": config('DB_HOST', default='localhost'),
           "port": config('DB_PORT', default='5432'),
           "user": config('DB_USER', default='postgres'),
           "password": config('DB_PASSWORD', default='7410'),
           "dbname": config('DB_NAME', default='postgres')}

DB_LOCATION = f"postgresql://{DB_INFO['user']}:{DB_INFO['password']}@{DB_INFO['host']}:" \
              f"{DB_INFO['port']}/{DB_INFO['dbname']}"
