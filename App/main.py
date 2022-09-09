from settings import *
import source_files as sc
import data_processing as dp
from load_db import create_db, create_tables, update_database


def main():
    print("Downloading files...")
    paths = sc.files_csv(URL_NAMES)
    print("Creating DataFrames...")
    df_general = dp.cleaning_data(paths)
    df_categoria = dp.qty_records_categoria(df_general)
    df_fuentes = dp.qty_records_fuente(df_general)
    df_provincia_categoria = dp.qty_records_provincia_categoria(df_general)
    df_cines = dp.processing_cines(paths[1])
    print('Creating DataBase...')
    create_db(DB_LOCATION)
    print('Creating tables...')
    create_tables(SQL_PATH)
    print("Updating records...")
    update_database(DB_LOCATION, df_general, "tabla_general")
    update_database(DB_LOCATION, df_categoria, "cant_categoria")
    update_database(DB_LOCATION, df_fuentes, "cant_fuente")
    update_database(DB_LOCATION, df_provincia_categoria, "cant_provincia_categoria")
    update_database(DB_LOCATION, df_cines, "salas_de_cine")
    print("Done.")


if __name__ == "__main__":
    main()
