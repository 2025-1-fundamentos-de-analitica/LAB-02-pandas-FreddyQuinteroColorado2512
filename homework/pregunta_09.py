def pregunta_09():
    """
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    ...
    """
    import pandas as pd

    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # No convertimos a datetime. Solo tomamos los primeros 4 caracteres del string.
    df['year'] = df['c3'].astype(str).str[:4]

    return df
