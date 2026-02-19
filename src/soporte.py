import pandas as pd


def analisis_rapido(df, n=5):

    """
    Función que proporciona un análisis rápido de un DataFrame.
    Parámetros:
    df: DataFrame a analizar.
    n: Número de filas (por defecto = 5)
    
    """

    print(f"Las {n} primeras columnas son:")
    display(df.head(n))
    print("Información básica del DataFrame:")
    display(df.info())
  
    print(f"El número de duplicados es: {df.duplicated().sum()}")
    display(df.isna().mean().round(4) * 100)