import pandas as pd


def cleaning_data(paths: list) -> pd.DataFrame:
    """
    :param: paths: list of file paths to clean
    :return: normalized general data frame
    """

    list_df = []
    for path in paths:
        file_name = path.split('/')[-1]
        category = file_name.split('-')[0]

        if category == 'bibliotecas':
            list_df.append(normalize_bibliotecas(path))

        elif category == 'cines':
            list_df.append(normalize_cines(path))

        elif category == 'museos':
            list_df.append(normalize_museos(path))

    general_df = pd.concat(list_df)

    return general_df


def normalize_bibliotecas(path) -> pd.DataFrame:

    df = pd.read_csv(path, encoding='UTF-8')
    df.drop(['Observacion', 'Subcategoria', 'Departamento', 'Piso', 'Cod_tel', 'Información adicional',
             'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Tipo_gestion', 'año_inicio',
             'Año_actualizacion'], axis=1, inplace=True)

    df.rename(columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia',
                       'IdDepartamento': 'id_departamento', 'Categoría': 'categoría',
                       'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Fuente': 'fuente',
                       'Domicilio': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono',
                       'Mail': 'mail', 'Web': 'web'}, inplace=True)
    return df


def normalize_cines(path) -> pd.DataFrame:

    df = pd.read_csv(path, encoding='UTF-8', header=None)
    headers_list = df.iloc[258]
    df.columns = headers_list

    df.rename(columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia',
                       'IdDepartamento': 'id_departamento', 'Categoría': 'categoría',
                       'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Fuente': 'fuente',
                       'Dirección': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono',
                       'Mail': 'mail', 'Web': 'web'}, inplace=True)

    df.drop(['Observaciones', 'Departamento', 'Piso', 'cod_area', 'Información adicional',
             'Latitud', 'Longitud', 'TipoLatitudLongitud', 'tipo_gestion', 'Pantallas',
             'Butacas', 'espacio_INCAA', 'año_actualizacion'], axis=1, inplace=True)

    df.drop([258], axis='index', inplace=True)

    return df


def normalize_museos(path) -> pd.DataFrame:

    df = pd.read_csv(path, encoding='UTF-8')
    df.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Info_adicional',
             'Latitud', 'Longitud', 'TipoLatitudLongitud', 'jurisdiccion', 'año_inauguracion',
             'actualizacion'], axis=1, inplace=True)

    df.rename(columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'categoria': 'categoría',
                       'IdDepartamento': 'id_departamento', 'direccion': 'domicilio', 'CP': 'código postal',
                       'telefono': 'número de teléfono', 'Mail': 'mail', 'Web': 'web'}, inplace=True)

    return df


def qty_records_categoria(df: pd.DataFrame) -> pd.DataFrame:
    df_categoria = df.value_counts('categoría').items()
    df_categoria = pd.DataFrame(df_categoria, columns=("categoría", "registros"))
    return df_categoria


def qty_records_fuente(df: pd.DataFrame) -> pd.DataFrame:
    df_fuente = df.value_counts('fuente').items()
    df_fuente = pd.DataFrame(df_fuente, columns=("fuente", "registros"))
    return df_fuente


def qty_records_provincia_categoria(df: pd.DataFrame) -> pd.DataFrame:
    df_provincia_categoria = df.value_counts(["provincia", "categoría"]).items()
    df_provincia_categoria = pd.DataFrame(df_provincia_categoria, columns=("provincia-categoria", "registros"))
    return df_provincia_categoria


def processing_cines(path) -> pd.DataFrame:

    df_cines = pd.read_csv(path, encoding='UTF-8', header=None)

    headers_list = df_cines.iloc[258]
    df_cines.drop([258], axis='index', inplace=True)
    df_cines.columns = headers_list
    df_cines = df_cines.loc[:, ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]

    df_cines['espacio_INCAA'].replace(to_replace='SI', value=True, inplace=True)
    df_cines['espacio_INCAA'].replace(to_replace='si', value=True, inplace=True)
    df_cines['espacio_INCAA'].replace(to_replace='0', value=False, inplace=True)
    df_cines['espacio_INCAA'].fillna(False, inplace=True)

    df_cines = df_cines.astype({'Pantallas': 'int', 'Butacas': 'int'})

    df_cines = df_cines.groupby(['Provincia'], as_index=False).sum()

    df_cines.rename(columns={'Pantallas': 'cantidad de pantallas', 'Butacas': 'cantidad de butacas',
                             'espacio_INCAA': 'cantidad de espacios INCAA'}, inplace=True)

    return df_cines
